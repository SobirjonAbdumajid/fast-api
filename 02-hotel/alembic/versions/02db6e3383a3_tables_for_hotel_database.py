"""tables for hotel database

Revision ID: 02db6e3383a3
Revises: a1d84f0ba14a
Create Date: 2024-12-19 10:03:22.776529

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '02db6e3383a3'
down_revision: Union[str, None] = 'a1d84f0ba14a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
