"""init migrations

Revision ID: 07a9d8fa9149
Revises: 
Create Date: 2024-11-12 01:39:32.952050

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa



revision: str = '07a9d8fa9149'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('documents_word',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('original_document', sa.String(), nullable=False),
    sa.Column('formatted_apa', sa.String(), nullable=True),
    sa.Column('formatted_something_else', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('documents_word')
    # ### end Alembic commands ###