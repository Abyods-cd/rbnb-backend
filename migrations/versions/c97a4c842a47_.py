"""empty message

Revision ID: c97a4c842a47
Revises: 
Create Date: 2024-09-14 21:23:34.791942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c97a4c842a47'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('icons', schema=None) as batch_op:
        batch_op.add_column(sa.Column('host_description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('icons', schema=None) as batch_op:
        batch_op.drop_column('host_description')

    # ### end Alembic commands ###
