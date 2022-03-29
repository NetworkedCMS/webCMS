"""empty message

Revision ID: 1fcee58045b3
Revises: 11b252ebcb47
Create Date: 2022-03-29 13:40:15.402641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fcee58045b3'
down_revision = '11b252ebcb47'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('content',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('html_content',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('template',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('css', sa.Column('html_content_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'css', 'html_content', ['html_content_id'], ['id'])
    op.add_column('footer_html', sa.Column('html_content_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'footer_html', 'html_content', ['html_content_id'], ['id'])
    op.add_column('header_html', sa.Column('html_content_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'header_html', 'html_content', ['html_content_id'], ['id'])
    op.add_column('navbar_html', sa.Column('html_content_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'navbar_html', 'html_content', ['html_content_id'], ['id'])
    op.add_column('page', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('page_sub_page_id_fkey', 'page', type_='foreignkey')
    op.create_foreign_key(None, 'page', 'users', ['user_id'], ['id'])
    op.drop_column('page', 'sub_page_id')
    op.add_column('template_settings', sa.Column('template_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'template_settings', 'template', ['template_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'template_settings', type_='foreignkey')
    op.drop_column('template_settings', 'template_id')
    op.add_column('page', sa.Column('sub_page_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'page', type_='foreignkey')
    op.create_foreign_key('page_sub_page_id_fkey', 'page', 'sub_page', ['sub_page_id'], ['id'])
    op.drop_column('page', 'user_id')
    op.drop_constraint(None, 'navbar_html', type_='foreignkey')
    op.drop_column('navbar_html', 'html_content_id')
    op.drop_constraint(None, 'header_html', type_='foreignkey')
    op.drop_column('header_html', 'html_content_id')
    op.drop_constraint(None, 'footer_html', type_='foreignkey')
    op.drop_column('footer_html', 'html_content_id')
    op.drop_constraint(None, 'css', type_='foreignkey')
    op.drop_column('css', 'html_content_id')
    op.drop_table('template')
    op.drop_table('html_content')
    op.drop_table('content')
    # ### end Alembic commands ###
