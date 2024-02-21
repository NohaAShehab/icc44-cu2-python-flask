"""add tracks to student

Revision ID: 54d4f5ba220b
Revises: 500fac0d9c4b
Create Date: 2024-02-21 09:44:18.615025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54d4f5ba220b'
down_revision = '500fac0d9c4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.add_column(sa.Column('track_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'tracks', ['track_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('track_id')

    # ### end Alembic commands ###
