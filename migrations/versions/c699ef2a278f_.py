"""empty message

Revision ID: c699ef2a278f
Revises: 76ae2cd14969
Create Date: 2021-10-30 23:45:13.865240

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c699ef2a278f'
down_revision = '76ae2cd14969'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('process', 'process_icon')
    op.add_column('process_title', sa.Column('image', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('process_title', 'image')
    op.add_column('process', sa.Column('process_icon', sa.VARCHAR(length=25), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
