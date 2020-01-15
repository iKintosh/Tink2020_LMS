"""add getters and setter in class User

Revision ID: ded18963434d
Revises: 5ecf30375af9
Create Date: 2020-01-13 18:19:40.872578

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ded18963434d'
down_revision = '5ecf30375af9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('course', 'name',
                    existing_type=sa.VARCHAR(),
                    nullable=False)
    op.alter_column('group', 'degree',
                    existing_type=sa.VARCHAR(),
                    nullable=False)
    op.alter_column('group', 'grade',
                    existing_type=sa.INTEGER(),
                    nullable=False)
    op.add_column('user', sa.Column('_User__facebook_link', sa.String(), nullable=True))
    op.add_column('user', sa.Column('_User__instagram_link', sa.String(), nullable=True))
    op.add_column('user', sa.Column('_User__linkedin_link', sa.String(), nullable=True))
    op.add_column('user', sa.Column('_User__password_hash', sa.String(), nullable=True))
    op.add_column('user', sa.Column('_User__phone', sa.String(), nullable=True))
    op.add_column('user', sa.Column('_User__vk_link', sa.String(), nullable=True))
    op.add_column('user', sa.Column('is_registered', sa.Boolean(), nullable=True))
    op.alter_column('user', 'family_name',
                    existing_type=sa.VARCHAR(),
                    nullable=False)
    op.alter_column('user', 'middle_name',
                    existing_type=sa.VARCHAR(),
                    nullable=False)
    op.alter_column('user', 'name',
                    existing_type=sa.VARCHAR(),
                    nullable=False)
    op.alter_column('user', 'verification_code',
                    existing_type=sa.VARCHAR(),
                    nullable=False)
    op.create_unique_constraint(None, 'user', ['email'])
    op.create_unique_constraint(None, 'user', ['verification_code'])
    op.drop_column('user', 'instagram_link')
    op.drop_column('user', 'facebook_link')
    op.drop_column('user', 'linkedin_link')
    op.drop_column('user', 'phone')
    op.drop_column('user', 'password_hash')
    op.drop_column('user', 'vk_link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('vk_link', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('password_hash', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('phone', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('linkedin_link', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('facebook_link', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('instagram_link', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'user', type_='unique')
    op.alter_column('user', 'verification_code',
                    existing_type=sa.VARCHAR(),
                    nullable=True)
    op.alter_column('user', 'name',
                    existing_type=sa.VARCHAR(),
                    nullable=True)
    op.alter_column('user', 'middle_name',
                    existing_type=sa.VARCHAR(),
                    nullable=True)
    op.alter_column('user', 'family_name',
                    existing_type=sa.VARCHAR(),
                    nullable=True)
    op.drop_column('user', 'is_registered')
    op.drop_column('user', '_User__vk_link')
    op.drop_column('user', '_User__phone')
    op.drop_column('user', '_User__password_hash')
    op.drop_column('user', '_User__linkedin_link')
    op.drop_column('user', '_User__instagram_link')
    op.drop_column('user', '_User__facebook_link')
    op.alter_column('group', 'grade',
                    existing_type=sa.INTEGER(),
                    nullable=True)
    op.alter_column('group', 'degree',
                    existing_type=sa.VARCHAR(),
                    nullable=True)
    op.alter_column('course', 'name',
                    existing_type=sa.VARCHAR(),
                    nullable=True)
    # ### end Alembic commands ###
