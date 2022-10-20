import asyncio
from flask import current_app
from aioflask.patched.flask_login import AnonymousUserMixin, UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from werkzeug.security import check_password_hash, generate_password_hash
from app.common.BaseModel import BaseModel
from app.utils.dep import login_manager
from sqlalchemy import Column, Boolean, String,ForeignKey, Integer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import relationship
from pydantic import EmailStr
from app.common.db import db_session as session


class Permission:
    GENERAL = 0x01
    ADMINISTER = 0xff


class Role(BaseModel):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    index = Column(String(64))
    default = Column(Boolean, default=False, index=True)
    permissions = Column(Integer)
    users = relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    async def insert_roles():
        roles = {
            'User': (Permission.GENERAL, 'main', True),
            'Administrator': (
                Permission.ADMINISTER,
                'admin',
                False  # grants all permissions
            )
        }
        for r in roles:
            role = await Role.get_by_field(r, 'name')
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.index = roles[r][1]
            role.default = roles[r][2]
            session.add(role)
        await session.commit()

    def __repr__(self):
        return '<Role \'%s\'>' % self.name


class User(UserMixin, BaseModel):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    confirmed = Column(Boolean, default=False)
    first_name = Column(String(64), index=True)
    last_name = Column(String(64), index=True)
    email = Column(String(64), unique=True, index=True)
    password_hash = Column(String(128))
    role_id = Column(Integer, ForeignKey('roles.id'))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)


    
    async def assign_role(self):
        if self.role == None:
            if self.email == current_app.config['ADMIN_EMAIL']:
                self.role = await Role.get_or_404(Permission.ADMINISTER, 
                'permissions')
        if self.role is None:
            self.role = await Role.get_or_404(True, 'default')
        session.add(self)
        await session.commit()
        await session.refresh(self)       
        


    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    async def can(self, access):
        role = await Role.get_by_contains(self, 'users')
        return role is not None and role.access_role == access \
             or role.access_role == Permission.ADMINISTER

    async def is_admin(self):
        return await self.can(Permission.ADMINISTER)

    @property
    def password(self):
        raise AttributeError('`password` is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self):
        """Generate a confirmation token to email a new user."""

        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'confirm': str(self.id)})

    def generate_email_change_token(self, new_email:EmailStr):
        """Generate an email change token to email an existing user."""
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'change_email': str(self.id), 'new_email': new_email})

    def generate_password_reset_token(self):
        """
        Generate a password reset change token to email to an existing user.
        """
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'reset': str(self.id)})

    async def confirm_account(self, token:str):
        """Verify that the provided token is for this user's id."""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except (BadSignature, SignatureExpired):
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        session.add(self)
        await session.commit()
        await session.refresh(self)
        return True

    async def change_email(self, token:str):
        """Verify the new email for this user."""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except (BadSignature, SignatureExpired):
            return False
        if data.get('change_email') != self.id:
            return False
        new_email = data.get('new_email')
        if new_email is None:
            return False
        if self.get_by_field(new_email, 'email', session) is not None:
            return False
        self.email = new_email
        session.add(self)
        await session.commit()
        await session.refresh(self)
        return True

    async def reset_password(self, token:str,
         new_password:str, session:AsyncSession ):
        """Verify the new password for this user."""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except (BadSignature, SignatureExpired):
            return False
        if data.get('reset') != self.id:
            return False
        self.password = new_password
        session.add(self)
        await session.commit()
        await session.refresh(self)
        return True

    @staticmethod
    def generate_fake(count=100, **kwargs):
        """Generate a number of fake users for testing."""
        from sqlalchemy.exc import IntegrityError
        from random import seed, choice
        from faker import Faker

        fake = Faker()
        roles = Role.query.all()

        seed()
        for i in range(count):
            u = User(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                password='password',
                confirmed=True,
                role=choice(roles),
                **kwargs)
            session.add(u)
            try:
                session.commit()
            except IntegrityError:
                session.rollback()

    def __repr__(self):
        return '<User \'%s\'>' % self.full_name()


class AnonymousUser(AnonymousUserMixin):
    def can(self, _):
        return False

    def is_admin(self):
        return False


login_manager.anonymous_user = AnonymousUser


def user_serializer(user):
    return {
        'id':user.id,
        'confirmed': user.confirmed,
        'first_name': user.first_name ,
        'last_name': user.last_name,
        'email': user.email ,
        'password_hash': user.password_hash ,
        'role_id': user.role_id,
        }

    


@login_manager.user_loader
def load_user(user_id):
    async def main()->User:
        return await User.get_or_none(user_id, 'id')   

    


    

    






class ApiKey(BaseModel):
    __tablename__ = 'api_keys'
    id = Column(Integer, primary_key=True)
    access_token = Column(String(500))
    #user_input = Column(String(500))
    #is_allowed = Column(Boolean, default=False)

    @staticmethod
    async def insert_key(session:AsyncSession):
        import secrets
        access_token = ApiKey(
            access_token = secrets.token_hex(),
            #is_allowed = True
        )
        session.add(access_token)
        await session.commit()
        await session.refresh(access_token)
        await session.flush()
        print('Created Api Access Key')

class ApiAccess(BaseModel):
    ''' Stores access key provided by the user who is trying to access the API'''
    __tablename__ = 'api_access'
    id = Column(Integer, primary_key=True)
    user_input = Column(String(500))
    is_allowed = Column(Boolean, default=False)
    session_id = Column(String(500))



