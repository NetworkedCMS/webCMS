"""empty message

Revision ID: 5c51c4e11c9b
Revises: d319adcc2828
Create Date: 2021-10-30 10:57:37.910632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c51c4e11c9b'
down_revision = 'd319adcc2828'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('process',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('steps', sa.String(length=120), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('process_icon', sa.String(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('process')
    # ### end Alembic commands ###
