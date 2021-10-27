"""empty message

Revision ID: fb1c0ae66490
Revises: 4c14cc854aad
Create Date: 2021-10-27 19:30:35.583194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb1c0ae66490'
down_revision = '4c14cc854aad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('call_to_action', sa.Column('is_login', sa.String(length=80), nullable=True))
    op.add_column('call_to_action', sa.Column('is_signup', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('call_to_action', 'is_signup')
    op.drop_column('call_to_action', 'is_login')
    # ### end Alembic commands ###
