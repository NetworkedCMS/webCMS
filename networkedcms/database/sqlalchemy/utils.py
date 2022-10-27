from math import ceil
from networkedcms.errors.models import DuplicatedEntryError
from sqlalchemy.exc import IntegrityError
from .db import Base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func




class Page(object):

    def __init__(self, items, page, page_size, total):
        self.data = items
        self.page = page
        self.page_size = page_size
        self.total = total
        self.previous_page = None
        self.previous_page = page - 1 if page > 1 else None
        #previous_items = (page - 1) * page_size
        #has_next = previous_items + len(items) < total
        self.next_page = page + 1 if self.has_next else None



    @property
    def pages(self):
        """The total number of pages"""
        if self.page_size == 0:
            pages = 0
        else:
            pages = int(ceil(self.total / float(self.page_size)))
        return pages

    def prev(self, error_out=False):
        """Returns a :class:`Pagination` object for the previous page."""
        assert self.items is not None, 'a query object is required ' \
                                       'for this method to work'
        return self.page - 1 if self.page > 1 else None

    @property
    def prev_num(self):
        """Number of the previous page."""
        if not self.has_prev:
            return None
        return self.page - 1

    @property
    def has_prev(self):
        """True if a previous page exists"""
        return self.page > 1

    def next(self, error_out=False):
        """Returns a :class:`Pagination` object for the next page."""
        assert self.items is not None, 'a query object is required ' \
                                       'for this method to work'
        return self.page + 1 if self.has_next else None

    @property
    def has_next(self):
        """True if a next page exists."""
        return self.page < self.pages

    @property
    def next_num(self):
        """Number of the next page"""
        if not self.has_next:
            return None
        return self.page + 1

    def iter_pages(self, left_edge=2, left_current=2,
                   right_current=5, right_edge=2):
        """Iterates over the page numbers in the pagination.  The four
        parameters control the thresholds how many numbers should be produced
        from the sides.  Skipped page numbers are represented as `None`.
        This is how you could render such a pagination in the templates:
        .. sourcecode:: html+jinja
            {% macro render_pagination(pagination, endpoint) %}
              <div class=pagination>
              {%- for page in pagination.iter_pages() %}
                {% if page %}
                  {% if page != pagination.page %}
                    <a href="{{ url_for(endpoint, page=page) }}">{{ page }}</a>
                  {% else %}
                    <strong>{{ page }}</strong>
                  {% endif %}
                {% else %}
                  <span class=ellipsis>…</span>
                {% endif %}
              {%- endfor %}
              </div>
            {% endmacro %}
        """
        last = 0
        for num in xrange(1, self.pages + 1):
            if num <= left_edge or \
               (num > self.page - left_current - 1 and
                num < self.page + right_current) or \
               num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num










class AsyncQueryMixin(object):
    """Mixin that adds convenience methods for CRUD (create, read, update, delete)
    operations.
    """

    @classmethod
    async def get_by_field(cls, value, field:str, session: AsyncSession):
        result = await session.execute(select(cls).where(getattr(cls, field)  == value ))
        return result.scalars().first()

    @classmethod
    async def get_all_by_field(cls, value, field:str, session: AsyncSession):
        result = await session.execute(select(cls).where(getattr(cls, field)  == value ))
        return result.scalars().all()    

    @classmethod
    async def get_by_contains(cls, value, field:str, session: AsyncSession):
        result = await session.execute(select(cls).where(getattr(cls, field).contains(value)))
        return result.scalars().first()  

    @classmethod
    async def get_all_by_multiple(cls, session, **kwargs):
        keys = await session.execute(select(cls).filter_by(**kwargs))
        return keys.scalars().all()

    @classmethod
    async def get_one_by_multiple(cls, session, **kwargs):
        keys = await session.execute(select(cls).filter_by(
        **kwargs))
        return keys.scalars().first()          



    @classmethod
    async def get_all(cls, session):
        total = await session.execute(select(cls).order_by(cls.id.desc()))
        return total.scalars().all()

    @classmethod
    async def total_count(cls, session):
        total = await session.execute(select(cls).order_by(cls.id.desc()))
        return len(total.scalars().all())    

    @classmethod
    async def paginate(cls, page, session, page_size=settings.PAGE_SIZE):
        if page <= 0:
            raise AttributeError('page needs to be >= 1')
        if page_size <= 0:
            raise AttributeError('page_size needs to be >= 1')
        
        items= await session.execute(select(cls).\
            limit(page_size).offset((page - 1) * page_size))
        items = items.scalars().all()
        total = await cls.total_count(session) 
        return Page(items, page, page_size, total)  
   

    @classmethod
    async def find_latest(cls, session):
        total = await session.execute(select(cls).order_by(cls.updated_at.desc()))
        return total.scalars().all()
      

    async def update(self, session, commit=True, **kwargs):
        """Update specific fields of a record."""
        # Prevent changing ID of object
        kwargs.pop('id', None)
        # Set latest updated_at
        kwargs['updated_at'] = func.now()
        for attr, value in kwargs.items():
            if value is not None:
                setattr(self, attr, value)
        return commit and await self.save(session) or self




    @classmethod
    async def create(cls, session,  **kwargs):
        """Create a new record and save it the database."""
        many = kwargs.get("many", None)
        if  many:
            kwargs.pop("many")
            instance = cls(**kwargs)
            return await instance.save_multiple(session=session)
        instance = cls(**kwargs)    
        return await instance.save(session=session)    

    async def save_multiple(self, session, commit=True):
        """Save the record."""
        session.add_all(self)
        if commit:
            try:
                await session.commit()       
            except IntegrityError as ex:
                await session.rollback()
                raise DuplicatedEntryError("The object is already stored")    
        return self    

    async def save(self, session, commit=True):
        """Save the record."""
        session.add(self)
        if commit:
            try:
                await session.commit()       
            except IntegrityError as ex:
                await session.rollback()
                raise DuplicatedEntryError("The object is already stored")    
        return self

    async def delete(self, session, commit=True):
        """Remove the record from the database."""
        await session.delete(self)
        await session.commit()

    """ Utility functions """
    @classmethod
    def date_to_string(cls, raw_date):
        return "{}".format(raw_date)