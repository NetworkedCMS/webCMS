import asyncio
from flask import current_app
from flask_login import AnonymousUserMixin, UserMixin
from importlib_metadata import files
from itsdangerous import URLSafeTimedSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from werkzeug.security import check_password_hash, generate_password_hash
from flask_tortoise import Model, fields
from tortoise.contrib.pydantic import pydantic_model_creator

from app.utils.dep import db, login_manager




class Permission:
    GENERAL = 'GENERAL'
    ADMINISTER = 'ADMINISTRATOR'
    MARKETERS = 'PROMOTER'
    EDITOR = 'EDITOR'
    CUSTOMERCARE = 'CUSTOMERCARE'

class Role(Model):
    #users = relationship('User', backref='role', lazy='dynamic')
    id = fields.IntField(pk=True, generated=True, unique=True)
    name = fields.CharField(max_length=50, null=False)
    index = fields.CharField(max_length=50, null=False)
    default = fields.BooleanField(default=False, index=True)
    access_role = fields.CharField(max_length=50, null=False,unique=True)
    permissions = fields.CharField(max_length=50, null=True)


    @classmethod
    async def insert_roles(cls):
        roles = {
            'User': (Permission.GENERAL, 'main', True),
            'Promoter': (Permission.MARKETERS, 'marketer',False ),
            'Editor': (Permission.EDITOR, 'editor',False ),
            'CustomerCare': (Permission.CUSTOMERCARE, 'customercare',False ),
            'Administrator': (
                Permission.ADMINISTER,
                'admin',
                False  # grants all permissions
            )
        }
        for r in roles:
            role = await Role.get_or_none(name=r)
            if role is None:
                role = await Role.create(name=r,
                    access_role = roles[r][0],
                    index = roles[r][1],
                    default = roles[r][2])    


    def __repr__(self):
        return '<Role \'%s\'>' % self.name



class User(UserMixin, Model):
    __tablename__ = 'users'
    id = fields.IntField(pk=True)
    confirmed = fields.BooleanField(default=False)
    first_name = fields.CharField(64, index=True)
    last_name = fields.CharField(64, index=True)
    email = fields.CharField(64, unique=True, index=True)
    password_hash = fields.CharField(128)
    role = fields.ForeignKeyField('models.Role', related_name="users", on_delete="CASCADE")
    
    def __str__(self) -> str:
        return self.full_name


    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    async def can(self, permissions):
        role = await Role.get_or_none(id=self.role_id)
        return role is not None and \
            (role.permissions & permissions) == permissions

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

    def generate_confirmation_token(self, expiration=604800):
        """Generate a confirmation token to email a new user."""

        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': str(self.id)})

    def generate_email_change_token(self, new_email, expiration=3600):
        """Generate an email change token to email an existing user."""
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'change_email': str(self.id), 'new_email': new_email})

    def generate_password_reset_token(self, expiration=3600):
        """
        Generate a password reset change token to email to an existing user.
        """
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': str(self.id)})

    async def confirm_account(self, token):
        """Verify that the provided token is for this user's id."""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except (BadSignature, SignatureExpired):
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        await self.save()
        return True

    async def change_email(self, token):
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
        if await self.get_or_none(email=new_email) is not None:
            return False
        self.email = new_email
        await self.save()
        return True

    async def reset_password(self, token, new_password):
        """Verify the new password for this user."""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except (BadSignature, SignatureExpired):
            return False
        if data.get('reset') != self.id:
            return False
        self.password = new_password
        await self.save()
        return True



class AnonymousUser(AnonymousUserMixin):
    def can(self, _):
        return False

    def is_admin(self):
        return False





async def load_user_(user_id):
    return await User.get_or_none(user_id)


login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(user_id):
    loop = asyncio.get_event_loop()
    print(loop)
    coroutine = load_user_(user_id)
    loop.run_until_complete(coroutine)




user_serializer = pydantic_model_creator(User, name="User")
UserOutput_Pydantic = pydantic_model_creator(User, name="UserOutput", exclude_readonly=True)



class ApiKey(Model):
    __tablename__ = 'api_keys'
    id = fields.IntField(pk=True)
    access_token = fields.CharField(500)
    #user_input = Column(String(500))
    #is_allowed = Column(Boolean, default=False)

    @staticmethod
    async def insert_key():
        import secrets
        access_token = ApiKey(
            access_token = secrets.token_hex(),
            #is_allowed = True
        )
        await access_token.save()
        print('Created Api Access Key')

class ApiAccess(Model):
    ''' Stores access key provided by the user who is trying to access the API'''
    __tablename__ = 'api_access'
    id = fields.IntField(pk=True)
    user_input = fields.CharField(500)
    is_allowed = fields.BooleanField(default=False)
    session_id = fields.CharField(500)
