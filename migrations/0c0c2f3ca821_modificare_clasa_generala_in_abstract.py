"""modificare clasa generala in abstract

Revision ID: 0c0c2f3ca821
Revises: 3044ff03a0e7
Create Date: 2024-03-18 12:37:00.377641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c0c2f3ca821'
down_revision = '3044ff03a0e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('general_registrations')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('general_registrations',
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
