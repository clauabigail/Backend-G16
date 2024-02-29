Este es mi repositorio del curso de Backend de CodiGo

Comandos semana07>

$ git status
$ git add -A
$ git commit -m "semana-06"
$ git push
$ git checkedout -b semana07

$ source entorno_django/Scripts/activate
$ pip install pillow
$ python manage.py makemigrations gestion --name creacion_tablas_ingredientes_preparaciones
$ python manage.py sqlmigrate gestion 0001
$ python manage.py migrate
$ python manage.py runserver
$ python manage.py shell
    >>> from gestion.models import Plato
    >>> Plato.objects.all()
    >>> nuevoPlato = Plato(nombre='Aji de gallina')
    >>> nuevoPlato.save()
    >>> Plato.objects.all()
    >>> exit()

 Jueves 22 de febrero 2024
 DRF Django RestFramework
 YASG para documentar   
 instalamos>
$ pip install drf-yasg



viernes 23 de febrero
$ python manage.py sqlmigrate gestion 0002
$ python manage.py makemigrations gestion --name agregue_columna_en_platos
$ python manage.py makemigrations gestion --name agregue_tabla_cheff
$ python manage.py showmigrations

        En terminal
            Microsoft Windows [Versión 10.0.19045.4046]
            (c) Microsoft Corporation. Todos los derechos reservados.

            C:\Users\Dell>pslq -U postgres
            "pslq" no se reconoce como un comando interno o externo,
            programa o archivo por lotes ejecutable.

            C:\Users\Dell>psql -U postgres
            Contraseña para usuario postgres:
            psql (16.2)
            Digite «help» para obtener ayuda.

            postgres=# DROP DATABASE recetario_db;
            DROP DATABASE
            postgres=# CREATE DATABASE recetario_db;
            CREATE DATABASE
            postgres=#
$ python manage.py migrate gestion
$ python manage.py migrate      
$ python manage.py createsuperuser
        correo>
        nombre>
        Password>
        y      

            psql -U postgres
Para la autenticacion (login), podemos usar una libreria  
pip install djangorestframework-simplejwt          