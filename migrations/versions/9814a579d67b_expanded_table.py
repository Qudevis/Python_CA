"""Expanded table

Revision ID: 9814a579d67b
Revises: 6e171361ced1
Create Date: 2024-06-12 11:13:46.330929

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9814a579d67b'
down_revision: Union[str, None] = '6e171361ced1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('People', sa.Column('Gender', sa.String(length=1), nullable=True))


def downgrade() -> None:
    op.drop_column('People', 'Gender')

    