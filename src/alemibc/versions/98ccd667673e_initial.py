"""initial

Revision ID: 98ccd667673e
Revises: 
Create Date: 2024-12-22 16:12:06.024292

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98ccd667673e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bets',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='Уникальный идентификатор'),
    sa.Column('event_id', sa.UUID(), nullable=False, comment='Id события'),
    sa.Column('amount', sa.DECIMAL(), nullable=False, comment='Сумма ставки'),
    sa.Column('status', sa.Enum('UNFINISHED', 'WON', 'LOST', name='betstatus'), nullable=False, comment='Статус ставки'),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='Дата создания'),
    sa.Column('updated_at', sa.DateTime(), nullable=True, comment='Дата обновления '),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bets')
    # ### end Alembic commands ###
