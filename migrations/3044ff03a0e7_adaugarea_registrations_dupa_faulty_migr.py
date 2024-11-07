"""adaugarea registrations dupa faulty migr

Revision ID: 3044ff03a0e7
Revises: 4573c03ad588
Create Date: 2024-03-18 12:35:09.949452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3044ff03a0e7'
down_revision = '4573c03ad588'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('germany_registrations')
    op.drop_table('france_registrations')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('france_registrations',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('country', sa.VARCHAR(length=50), nullable=True),
    sa.Column('registration_type', sa.VARCHAR(length=50), nullable=True),
    sa.Column('minimum_diesel', sa.VARCHAR(length=50), nullable=True),
    sa.Column('minimum_petrol', sa.VARCHAR(length=50), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('image_url', sa.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('germany_registrations',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('country', sa.VARCHAR(length=50), nullable=True),
    sa.Column('registration_type', sa.VARCHAR(length=50), nullable=True),
    sa.Column('minimum_diesel', sa.VARCHAR(length=50), nullable=True),
    sa.Column('minimum_petrol', sa.VARCHAR(length=50), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('image_url', sa.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###