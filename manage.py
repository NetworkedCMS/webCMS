#!/usr/bin/env python
import os, asyncio
import subprocess
import click
from app.main import create_app
from app.models.users import Role, User, ApiKey
from config import Config

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')


@app.cli.command("shell_context")
def make_shell_context():
    return dict(app=app,User=User, Role=Role)


@click.group()
def cli():
    pass

@cli.command()
def add_api_key():
    """
    Adds Api key to the database.
    """
    asyncio.run(ApiKey.insert_key())

@cli.command()
def test():
    """Run the unit tests."""
    import unittest

    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@cli.command()
def runserver():
    app.run()


@cli.command
def recreate_db():
    """
    Recreates a local database. You probably should not use this on
    production.
    """
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.commit()
        db.session.flush()


@cli.command()
def create_tables():
    """
    Recreates a local database's tables without dropping the database.
    """
    db.create_all()
    db.session.commit()




@cli.command
def setup_dev():
    """Runs the set-up needed for local development."""
    asyncio.run(setup_general())


@cli.command
def setup_prod():
    """Runs the set-up needed for production."""
    asyncio.run(setup_general())


async def setup_general():
    """Runs the set-up needed for both local development and production.
       Also sets up first admin user."""
    await Role.insert_roles()
    admin_query = await Role.get_or_none(name='Administrator')
    if admin_query is not None:
        if await User.get_or_none(email=Config.ADMIN_EMAIL).first() is None:
            user = User(
                first_name='Admin',
                last_name='Account',
                password=Config.ADMIN_PASSWORD,
                confirmed=True,
                email=Config.ADMIN_EMAIL)
            await user.save()
            print('Added administrator {}'.format(user.full_name()))





@cli.command
def format():
    """Runs the yapf and isort formatters over the project."""
    isort = 'isort -rc *.py app/'
    yapf = 'yapf -r -i *.py app/'

    print('Running {}'.format(isort))
    subprocess.call(isort, shell=True)

    print('Running {}'.format(yapf))
    subprocess.call(yapf, shell=True)


if __name__ == '__main__':
    cli()







