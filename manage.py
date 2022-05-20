#!/usr/bin/env python
import os, asyncio
import subprocess
import click, uvicorn
from app import create_app
from app.models import Role, User, ApiKey
from config import Config
from asgiref.wsgi import WsgiToAsgi
from app.common.db import db_session, init_models

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
    async def main():
        
        await ApiKey.insert_key(db_session)
        await db_session.close()
    asyncio.run(main())        

@cli.command()
def test():
    """Run the unit tests."""
    import unittest

    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@cli.command()
def runserver():
    app.run(host="0.0.0.0",  port=5000, reload=True,
         debug=True,log_level="info", app='manage:app', )     


@cli.command
def recreate_db():
    """
    Recreates a local database. You probably should not use this on
    production.
    """
    asyncio.run(init_models())





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
      
    await Role.insert_roles(db_session)
    admin_query = await Role.get_by_field('Administrator', 'name', db_session)
    if admin_query is not None:
        if await User.get_by_field(Config.ADMIN_EMAIL, 'email', db_session) is None:
            user = await User.create(db_session,
            **dict(first_name='Admin',
                last_name='Account',
                password=Config.ADMIN_PASSWORD,
                confirmed=True,
                email=Config.ADMIN_EMAIL)
             )
            print('Added administrator {}'.format(user.full_name()))
    await db_session.close()


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







