"""empty message

Revision ID: 315393451125
Revises: cdfc1349aee6
Create Date: 2020-07-08 22:41:58.995779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '315393451125'
down_revision = 'cdfc1349aee6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'seeking_description')
    # ### end Alembic commands ###