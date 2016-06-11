"""empty message

Revision ID: 7c5b7bf1d397
Revises: b2d315470289
Create Date: 2016-06-11 16:48:06.803674

"""

# revision identifiers, used by Alembic.
revision = '7c5b7bf1d397'
down_revision = 'b2d315470289'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    ### end Alembic commands ###
