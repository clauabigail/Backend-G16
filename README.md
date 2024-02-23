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