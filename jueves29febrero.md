Express con Prisma

PS D:\Abigail Curso Web full stack TECSUP 2023\bootcamp-backend-g16\Backend-G16-semana08\introduccion_express> cd ..
PS D:\Abigail Curso Web full stack TECSUP 2023\bootcamp-backend-g16\Backend-G16-semana08> cd express_con_prisma
PS D:\Abigail Curso Web full stack TECSUP 2023\bootcamp-backend-g16\Backend-G16-semana08\express_con_prisma> npm init

ORM para NodeJS
https://www.prisma.io/orm

    npm i prisma

cuando no reconoce npm :
    nvs use latest
    node --version


npm > node package manaer
npx > node package executer

para usar Prisma, usamos un 
   npx  prisma > NOS DA LA documentacionPRISMA
            Commands

            init   Set up Prisma for your app
        generate   Generate artifacts (e.g. Prisma Client)
              db   Manage your database schema and lifecycle
         migrate   Migrate your database
          studio   Browse your data with Prisma Studio
        validate   Validate your Prisma schema
          format   Format your Prisma schema
         version   Displays Prisma version info
           debug   Displays Prisma debug info

    npx prisma init       
        instalar la extension Prisma para que aparezca en colores el editor de codigo

dbdiagram.io > para diseñar nuestra BD

en el archivo schema.prisma > generamnos el ORM > modelo de tablas
Luego en una terminal  > para generar nuesta BD en  Postgres
            Microsoft Windows [Versión 10.0.19045.4046]
(c) Microsoft Corporation. Todos los derechos reservados.

C:\Users\Dell>psql -U postgres
Contraseña para usuario postgres:
psql (16.2)
Digite «help» para obtener ayuda.

postgres=# CREATE DATABASE minimarket;
CREATE DATABASE
postgres=#

Instalamos la libreria  
npm i dotenv  > para leer variables de entorno

En la terminal de Visaual Studio>
npx prisma init             > inicializamos prisma
npx prisma migrate dev 

npm i express
npm i --save-dev @types/express nodemon

Librerias para validacion la informacion que viene de mi cliente, con una serie de pasos:
zod / yup / joi
Usaremnos joi       https://joi.dev/

    npm i joi



                Operaciones basicas de psql (consola)
                \l Te muestra las bases de datos existentes.
                \d Te muestra las relaciones (tablas, secuencias, etc.) existentes en la base de datos.
                \d [nombre_tabla]  Para ver la descripción (nombre de columnas, tipo de datos, etc.) de una tabla.
                \c [nombre_bd]     Para conectarte a otra base de datos.
                SHOW search_path;  Para ver la ruta de búsqueda actual.
                SET search_path TO [nombre_esquema]; Para actualizar la ruta de búsqueda.
                \q                Para salir de psql



libreria para manejar errores: expres-async-handler
instalamos npm i express-async-handler
