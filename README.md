# Service example
todo funciona con django 1.11
probado en python 2.7
el requeriments tiene lo necesario

primero correr 
python manage.py consumir

luego en otra terminal

python manage.py runserver


Todo funciona con ajax.
abrir el navegador sobre http://127.0.0.1:8000/
requiere internet para descargar la lib "https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js" sobre el browser
si se quisiera mejorar mas , se podria colocar un setinterval para refrescar o utilizar webworkers .



las api rest framework  http://127.0.0.1:8000/api/v1/  , muestra todos los datos.
consulta la informacion http://127.0.0.1:8000/api/v1/buscar/(aqui colocamos el ticker)/ 