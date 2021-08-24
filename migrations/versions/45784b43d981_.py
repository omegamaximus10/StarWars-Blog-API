"""empty message

Revision ID: 45784b43d981
Revises: 
Create Date: 2021-08-24 19:05:23.905685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45784b43d981'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('gender', sa.String(length=200), nullable=False),
    sa.Column('height', sa.String(length=200), nullable=False),
    sa.Column('birth_year', sa.String(length=100), nullable=False),
    sa.Column('hair_color', sa.String(length=200), nullable=False),
    sa.Column('skin_color', sa.String(length=200), nullable=False),
    sa.Column('eye_color', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=400), nullable=False),
    sa.Column('diameter', sa.Integer(), nullable=False),
    sa.Column('climate', sa.String(length=400), nullable=False),
    sa.Column('gravity', sa.String(length=400), nullable=False),
    sa.Column('terrain', sa.String(length=400), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('email')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('people_id', sa.Integer(), nullable=True),
    sa.Column('planets_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['people_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['planets_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorites')
    op.drop_table('user')
    op.drop_table('planets')
    op.drop_table('people')
    # ### end Alembic commands ###
