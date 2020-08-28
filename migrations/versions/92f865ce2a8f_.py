"""empty message

Revision ID: 92f865ce2a8f
Revises: 4598f56892cf
Create Date: 2020-07-09 17:31:51.505562

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92f865ce2a8f'
down_revision = '4598f56892cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'Venue', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Venue', type_='unique')
    # ### end Alembic commands ###
