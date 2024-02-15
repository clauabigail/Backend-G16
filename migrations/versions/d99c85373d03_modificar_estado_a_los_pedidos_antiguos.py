"""modificar estado a los pedidos antiguos

Revision ID: d99c85373d03
Revises: 0486f5ec6457
Create Date: 2024-02-08 19:38:48.067317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd99c85373d03'
down_revision = '0486f5ec6457'
branch_labels = None
depends_on = None


def upgrade():
    # si queremos realizar en la migracion un comando de ejecucion SQL podemos usar el metodo execute
    op.execute("UPDATE pedidos SET estado = 'EN_ESPERA' WHERE estado IS NULL")


def downgrade():
    pass
