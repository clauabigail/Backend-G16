-- SQL > Structured Query Language

-- DML 
-- Data Manipulation Language (Lenguaje de manipulacion de Datos)

-- DDL
-- Data Definition Language (Lenguaje de Definicion de Datos)
-- Sirve para indicar como se almacenaran los datos para definir las columnas
-- Tablas entre otros
-- Los comandos en SQL tienen que3 finalizar con el ;
-- IF NOT EXISTS sirve para comandos de CREACION (BD, TABLAS, COLUMNAS)
create database if not exists pruebas;

-- Seleccionamos en que base de datos vamos a trabajar
USE pruebas;

CREATE TABLE personas (
	id 					INT 		PRIMARY KEY AUTO_INCREMENT, -- Forma de declarar primary Key dentro de la misma linea de codigo 
    nombre 				TEXT		NULL,
    apellido 			VARCHAR(50),
    fecha_nacimiento	DATE,
    nacionalidad		VARCHAR(100) DEFAULT 'PERUANO'
    -- PRIMARY KEY (id) -- Forma aislada
);

-- DML
-- Data Manipulation Language (Lenguaje de Manipulacion de Datos)

-- Agregar informacion a la tabla
INSERT INTO personas 	(id, nombre, apellido, fecha_nacimiento) VALUES
						(DEFAULT, 'Eduardo', 'de Rivero', '1992-08-01' );

-- Si no declaro las columnas que voy a insertar me veo en la OBLIGACION de colocar valores
-- a todas las columnas y siguiendo el mismo orden que use al momento de crear la tabla
INSERT INTO personas VALUES (DEFAULT, 'Juana', 'Martinez', '2004-02-10', 'Uruguayo');

INSERT INTO personas 	(nombre, apellido, fecha_nacimiento, nacionalidad) VALUES
						('Bryan', 'Urquizo', '1995-02-01', 'PERUANO' ),
                        ('Maria', 'Retamozo', '1989-06-14', 'SALVADOREÑA' );

SELECT * FROM personas;	

SELECT * -- columnas
FROM personas -- tabla
WHERE nombre = 'Eduardo'; -- condicional

SELECT *
FROM personas
WHERE nacionalidad = 'Peruano' AND id=3;

SELECT * FROM personas WHERE nombre LIKE '%a%';

SELECT * FROM personas WHERE nombre LIKE '%__u%'; -- Buscar la u en la tercera posicion del campo nombre, usamos guin bajo para indicar el numero de espacios

-- Devolver todas las personas cuyo nombre tenga la letra 'r' o en su apellido tenga
-- la letra 'a'
SELECT * FROM personas WHERE nombre LIKE '%r%' OR apellido LIKE '%a%';

SELECT * FROM personas WHERE id IN(1,2,3); -- esta es mas eficiente  que la siguiente consulta
SELECT * FROM personas WHERE id=1 OR id=2 OR id=3;

SELECT *
FROM personas
LIMIT 2		-- 2 elementos por pagina
OFFSET 2;	-- Offset sirve para indicar cuantos se tiene que saltar	

-- Actualizaciones
UPDATE personas
SET nombre = 'Rodrigo' , apellido = 'Flores'
WHERE id = 1;

SELECT * FROM personas WHERE id = 1;

DELETE FROM personas WHERE id = 4;
SELECT * FROM personas;

-- DIRECCIONES



