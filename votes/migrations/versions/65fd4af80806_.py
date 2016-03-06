"""empty message

Revision ID: 65fd4af80806
Revises: cb9ff1f36cc1
Create Date: 2016-03-06 16:32:14.434023

"""

# revision identifiers, used by Alembic.
revision = '65fd4af80806'
down_revision = 'cb9ff1f36cc1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('name', sa.String(length=100), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('item', 'name')
    ### end Alembic commands ###