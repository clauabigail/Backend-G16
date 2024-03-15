-- AlterTable
ALTER TABLE "detalle_pedidos" RENAME CONSTRAINT "DetallePedido_pkey" TO "detalle_pedidos_pkey";

-- RenameForeignKey
ALTER TABLE "detalle_pedidos" RENAME CONSTRAINT "DetallePedido_pedido_id_fkey" TO "detalle_pedidos_pedido_id_fkey";

-- RenameForeignKey
ALTER TABLE "detalle_pedidos" RENAME CONSTRAINT "DetallePedido_producto_id_fkey" TO "detalle_pedidos_producto_id_fkey";
