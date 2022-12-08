SELECT Categoria.Nombre
FROM Categoria
WHERE CodigoCategoria =(
    Select Producto.CodigoCategoria
    From Producto
    where Producto.CodigoProducto = 
    (
        SELECT Venta.CodigoProducto
        from Venta
        WHERE Fecha=(
            select MAX(Venta.Fecha)
            from Venta)
        )
);