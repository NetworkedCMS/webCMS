import os

from aioflask import render_template
from flask_mail import Message

from app import create_app, mail


async def send_email(recipient, subject, template, **kwargs):
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    with app.app_context():
        msg = Message(
            app.config['EMAIL_SUBJECT_PREFIX'] + ' ' + subject,
            sender=app.config['EMAIL_SENDER'],
            recipients=[recipient])
        msg.body = await render_template(template + '.txt', **kwargs)
        msg.html = await render_template(template + '.html', **kwargs)
        mail.send(msg)
