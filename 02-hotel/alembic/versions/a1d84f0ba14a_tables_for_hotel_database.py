"""tables for hotel database

Revision ID: a1d84f0ba14a
Revises: bc7ddfa9fe79
Create Date: 2024-12-19 09:56:22.382041

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1d84f0ba14a'
down_revision: Union[str, None] = 'bc7ddfa9fe79'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
