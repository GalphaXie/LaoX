"""roles_rename_nick_name

Revision ID: 873bc770ef76
Revises: 9c9ff7c6d865
Create Date: 2018-04-14 11:29:30.656960

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '873bc770ef76'
down_revision = '9c9ff7c6d865'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('nick_name', sa.String(length=64), nullable=True))
    op.drop_index('name', table_name='roles')
    op.create_unique_constraint(None, 'roles', ['nick_name'])
    op.drop_column('roles', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('name', mysql.VARCHAR(length=64), nullable=True))
    op.drop_constraint('nick_name', 'roles', type_='unique')
    op.create_index('name', 'roles', ['name'], unique=True)
    op.drop_column('roles', 'nick_name')
    # ### end Alembic commands ###
