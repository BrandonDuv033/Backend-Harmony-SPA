"""Index user's last name.

Revision ID: e21f6c84a903
Revises: bd044bb45e2f
Create Date: 2026-11-24
"""
from typing import Sequence, Union

from alembic import op


revision: str = "e21f6c84a903"
down_revision: Union[str, Sequence[str], None] = "bd044bb45e2f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_index("ix_users_last_name", "users", ["last_name"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_users_last_name", table_name="users")
