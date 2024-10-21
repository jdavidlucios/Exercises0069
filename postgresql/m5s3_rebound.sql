-- Tabla Empresa
CREATE TABLE Empresa (
    RUT VARCHAR(10) PRIMARY KEY,
    Nombre VARCHAR(120),
    Direccion VARCHAR(120),
    Telefono VARCHAR(15),
    Correo VARCHAR(50),
    Web VARCHAR(50)
);

-- Tabla Cliente
CREATE TABLE Cliente (
    RUT VARCHAR(10) PRIMARY KEY,
    Nombre VARCHAR(120),
    Correo VARCHAR(50),
    Direccion VARCHAR(120),
    Celular VARCHAR(12),
    Alta DATE
);

-- Tabla TipoVehiculo
CREATE TABLE TipoVehiculo (
    IDTipoVehiculo BIGINT PRIMARY KEY,
    Nombre VARCHAR(120)
);

-- Tabla Marca
CREATE TABLE Marca (
    IDMarca BIGINT PRIMARY KEY,
    Nombre VARCHAR(120)
);

-- Tabla Vehiculo
CREATE TABLE Vehiculo (
    IDVehiculo BIGINT PRIMARY KEY,
    Patente VARCHAR(10),
    Marca VARCHAR(120),
    Modelo VARCHAR(120),
    Color VARCHAR(120),
    Precio NUMERIC(12, 2),  -- Precio decimal
    FrecuenciaMantenimiento INTEGER,  -- Entero pequeño
    IDTipoVehiculo BIGINT,
    IDMarca BIGINT,
    CONSTRAINT Vehiculo_TipoVehiculo_FK FOREIGN KEY (IDTipoVehiculo) REFERENCES TipoVehiculo(IDTipoVehiculo),
    CONSTRAINT Vehiculo_Marca_FK FOREIGN KEY (IDMarca) REFERENCES Marca(IDMarca)
);

-- Tabla Venta
CREATE TABLE Venta (
    Folio BIGINT PRIMARY KEY,
    Fecha DATE,
    Monto NUMERIC(12, 2),  -- Valor decimal
    Vehiculo_IDVehiculo BIGINT,
    Cliente_RUT VARCHAR(10),
    CONSTRAINT Venta_Cliente_FK FOREIGN KEY (Cliente_RUT) REFERENCES Cliente(RUT),
    CONSTRAINT Venta_Vehiculo_FK FOREIGN KEY (Vehiculo_IDVehiculo) REFERENCES Vehiculo(IDVehiculo)
);

-- Tabla Mantencion
CREATE TABLE Mantencion (
    IDMantencion BIGINT PRIMARY KEY,
    Fecha DATE,
    TrabajosRealizados VARCHAR(1000),
    Venta_Folio BIGINT,
    CONSTRAINT Mantencion_Venta_FK FOREIGN KEY (Venta_Folio) REFERENCES Venta(Folio)
);
