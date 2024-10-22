-- 1. Crear la base de datos llamada empresa
CREATE DATABASE empresa;

-- Conectarse a la base de datos empresa
-- \c empresa; (en terminal psql)

-- 2. Crear la tabla departamentos
CREATE TABLE departamentos (
    id SERIAL PRIMARY KEY,     -- id entero, clave primaria con serial auto-incremental
    nombre VARCHAR(100) NOT NULL, -- nombre (cadena de caracteres, hasta 100 caracteres)
    ubicacion VARCHAR(100)          -- ubicacion (cadena de caracteres, hasta 100 caracteres)
);

-- 3. Crear la tabla empleados
CREATE TABLE empleados (
    id SERIAL PRIMARY KEY,         -- id entero, clave primaria con serial auto-incremental
    nombre VARCHAR(100) NOT NULL,  -- nombre (cadena de caracteres, hasta 100 caracteres)
    puesto VARCHAR(100) NOT NULL,  -- puesto (cadena de caracteres, hasta 100 caracteres)
    salario DECIMAL(10, 2),        -- salario (decimal, hasta 10 dígitos enteros y 2 decimales)
    fecha_contratacion DATE,       -- fecha_contratacion (fecha)
    departamento_id INT,           -- departamento_id (entero, clave foránea que referencia departamentos.id)
    CONSTRAINT fk_departamento FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
);

-- 4. Modificar la tabla empleados para agregar la columna email
ALTER TABLE empleados
ADD COLUMN email VARCHAR(100);  -- agregar columna email (cadena de caracteres, hasta 100 caracteres)

-- 5. Cambiar el nombre de la tabla empleados a trabajadores
ALTER TABLE empleados
RENAME TO trabajadores;

-- 6. Eliminar la tabla departamentos
DROP TABLE departamentos CASCADE;
