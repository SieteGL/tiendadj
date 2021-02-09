# tiendadj
Proyecto Django para la sección de servicios Rest DRF en curso profesional 

crear entorno virtual 

linux| python3 -m venv "nombre entorno"

windows| python -m venv "nombre entorno" Sin comillas

realizar instalacion de required ubicarse sobre carpeta required y ejecutar el comando

pip install -r local.txt

si se escuentra en OS como linux-ubuntu o deribados, 

modificar psycopg2==2.8.5 --> psycopg2-binary==2.8.5

crear base de datos en postgresql 'agendabd'

realizar migraciones si es necesario

python manage.py makemigrations
python manage.py migrate

crear superusuario para acceder a Django admin

python manage.py runserver

revisar terminal para corregir posibles problemas que arroje la terminal

