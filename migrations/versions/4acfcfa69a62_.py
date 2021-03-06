"""empty message

Revision ID: 4acfcfa69a62
Revises: 02ccb3e6a553
Create Date: 2016-05-25 16:28:16.745806

"""

# revision identifiers, used by Alembic.
revision = '4acfcfa69a62'
down_revision = '02ccb3e6a553'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    ### end Alembic commands ###
