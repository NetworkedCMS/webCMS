"""empty message

Revision ID: 271a8f35cf7e
Revises: 39f347b45eb9
Create Date: 2022-03-29 14:50:41.688310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '271a8f35cf7e'
down_revision = '39f347b45eb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('footer_html', sa.Column('html_content_id', sa.Integer(), nullable=True))
    op.drop_constraint('footer_html_footer_html_content_id_fkey', 'footer_html', type_='foreignkey')
    op.create_foreign_key(None, 'footer_html', 'html_content', ['html_content_id'], ['id'])
    op.drop_column('footer_html', 'footer_html_content_id')
    op.add_column('header_html', sa.Column('html_content_id', sa.Integer(), nullable=True))
    op.drop_constraint('header_html_header_html_content_id_fkey', 'header_html', type_='foreignkey')
    op.create_foreign_key(None, 'header_html', 'html_content', ['html_content_id'], ['id'])
    op.drop_column('header_html', 'header_html_content_id')
    op.add_column('navbar_html', sa.Column('html_content_id', sa.Integer(), nullable=True))
    op.drop_constraint('navbar_html_navbar_html_content_id_fkey', 'navbar_html', type_='foreignkey')
    op.create_foreign_key(None, 'navbar_html', 'html_content', ['html_content_id'], ['id'])
    op.drop_column('navbar_html', 'navbar_html_content_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('navbar_html', sa.Column('navbar_html_content_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'navbar_html', type_='foreignkey')
    op.create_foreign_key('navbar_html_navbar_html_content_id_fkey', 'navbar_html', 'html_content', ['navbar_html_content_id'], ['id'])
    op.drop_column('navbar_html', 'html_content_id')
    op.add_column('header_html', sa.Column('header_html_content_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'header_html', type_='foreignkey')
    op.create_foreign_key('header_html_header_html_content_id_fkey', 'header_html', 'html_content', ['header_html_content_id'], ['id'])
    op.drop_column('header_html', 'html_content_id')
    op.add_column('footer_html', sa.Column('footer_html_content_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'footer_html', type_='foreignkey')
    op.create_foreign_key('footer_html_footer_html_content_id_fkey', 'footer_html', 'html_content', ['footer_html_content_id'], ['id'])
    op.drop_column('footer_html', 'html_content_id')
    # ### end Alembic commands ###
