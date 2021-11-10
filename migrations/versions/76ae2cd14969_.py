"""empty message

Revision ID: 76ae2cd14969
Revises: 3567286c82e8
Create Date: 2021-10-30 12:31:41.036916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76ae2cd14969'
down_revision = '3567286c82e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('process', sa.Column('description', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('process', 'description')
    # ### end Alembic commands ###