"""empty message

Revision ID: fe4ab2ed260f
Revises: d7288f77b7b2
Create Date: 2022-09-05 10:39:42.136788

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe4ab2ed260f'
down_revision = 'd7288f77b7b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('beer_details',
    sa.Column('rec_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('rec_id')
    )
    op.create_index(op.f('ix_beer_details_name'), 'beer_details', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_beer_details_name'), table_name='beer_details')
    op.drop_table('beer_details')
    # ### end Alembic commands ###
