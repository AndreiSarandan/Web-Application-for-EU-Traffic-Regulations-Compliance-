"""Addd oficial page column.

Revision ID: 8e70eb170ed9
Revises: f31b07641a49
Create Date: 2024-03-02 19:36:34.566309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e70eb170ed9'
down_revision = 'f31b07641a49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('zone', schema=None) as batch_op:
        batch_op.add_column(sa.Column('official_page', sa.String(length=150), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('zone', schema=None) as batch_op:
        batch_op.drop_column('official_page')

    # ### end Alembic commands ###
