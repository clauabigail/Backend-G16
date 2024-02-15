"""agregue valor defult al estado

Revision ID: 0486f5ec6457
Revises: cdd0a6d718ba
Create Date: 2024-02-08 19:33:08.012666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0486f5ec6457'
down_revision = 'cdd0a6d718ba'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(table_name='pedidos', column_name='estado',
                    server_default='EN_ESPERA')


def downgrade():
    op.alter_column(table_name='pedidos',
                    column_name='estado',server_default='None')
