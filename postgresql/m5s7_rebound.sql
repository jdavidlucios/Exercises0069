SELECT 
    Nombre, RUT 
FROM 
    Cliente 
WHERE 
    RUT NOT IN (SELECT Cliente_RUT FROM Venta);

SELECT 
    v.Folio, 
    v.Fecha, 
    v.Monto, 
    c.Nombre AS NombreCliente, 
    c.RUT AS RutCliente 
FROM 
    Venta v 
JOIN 
    Cliente c 
ON 
    v.Cliente_RUT = c.RUT;
SELECT 
    c.Nombre AS NombreCliente, 
    c.RUT AS RutCliente,
    SUM(v.Monto) AS TotalVentasAnuales,
    CASE 
        WHEN SUM(v.Monto) <= 1000000 THEN 'Standar'
        WHEN SUM(v.Monto) BETWEEN 1000001 AND 3000000 THEN 'Gold'
        ELSE 'Premium'
    END AS Clasificacion
FROM 
    Cliente c 
LEFT JOIN 
    Venta v 
ON 
    c.RUT = v.Cliente_RUT
GROUP BY 
    c.Nombre, c.RUT;

SELECT 
    v.Folio, 
    v.Fecha, 
    v.Monto, 
    ve.Marca
FROM 
    Venta v 
JOIN 
    Vehiculo ve 
ON 
    v.Vehiculo_IDVehiculo = ve.IDVehiculo
WHERE 
    ve.Marca = (
        SELECT 
            ve.Marca 
        FROM 
            Venta v 
        JOIN 
            Vehiculo ve 
        ON 
            v.Vehiculo_IDVehiculo = ve.IDVehiculo 
        GROUP BY 
            ve.Marca 
        ORDER BY 
            COUNT(ve.Marca) DESC 
        LIMIT 1
    );
