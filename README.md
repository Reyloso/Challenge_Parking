# Parking 📋
```bash
# Introduccion
Sistema  para gestión y administración de un parqueadero

En Este Blog se pueden publicar posts Y filtrar por titulo y autor+
se manejan 3 tipos de usuarios (ADMINISTRADOR, CONSERJE y EMPLEADO)
ADMINISTRADOR:
Tiene acceso a todo el sistema incluyendo los reportes

CONSERJE:
Puede crear vehiculos, celdas,  crear y asignar empleados a vehiculos etc, no puede ver reportes.

EMPLEADO:
Puede crear vehiculos, y puede solo ver sus vehiculos.


```

### Requerimientos 📋
```
Python 3.5 o superior
django 2.2.9 LTS
django-extensions
psycopg2 2.8.4 o superior

```

### Installation 🔧
- Clonar el repositorio
```bash
    git@github.com:Reyloso/parking_challenge.git

# Crear entorno virtual y activar
pip install virtualenv MiEntorno
#para windows
cd /miEntorno/scripts
activate

#para linux
cd /miEntorno/bin
source activate

```
- Clonar el repositorio
```bash
    pip install -r requierements.txt
```
## Configurar la Base de datos Posgres ⚙️
- Modificar el archivo settings.py 
- Reemplazar datos por los que tenga configurado en la base de datos
```bash
# Primero crear la base de datos y luego cambiar los datos en el archivo settings.py

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': 'parkin',
         'USER': 'postgres',
         'PASSWORD': '123456',
         'HOST': 'localhost',
         'PORT': '5432',
     }
 }

```

### Crear Migraciones y Luego migrar a la base de datos 🔩

```
python manage.py makemigrations parking, employees
python manage.py migrate
```
##  Ejecutar script para configuracion inicial🚀
```bash
# Creacion tipos de documentos, usuarios, celdas y vehiculos
python manage.py runscript config

```
##  Despliegue 🚀

```
Python manage.py runserver 
```

## Acceder al sistema 
```bash
# Copiar esta ruta en el navegador
http://127.0.0.1:8000/
# luego paraa acceder al sistema puede acceder con estos tipos de usuarios: 
# ADMINISTRADOR
usuario: admin
contraseña: qwerty123
# CONCERJE
usuario: concerje
contraseña: qwerty123
# EMPLEADO
usuario: pablo
contraseña: qwerty123
```
## Construido con 🛠️

* [Django](https://docs.djangoproject.com/en/2.2/) -  El framework web usado
* [Git](https://getbootstrap.com/) - Controlador de Versiones



## Autor ✒️
* **Reinaldo Lopez** 

## Expresiones de Gratitud 🎁

* Muchas Gracias 🤓.
---
⌨️ Por [Reinaldo Lopez](https://github.com/Reyloso/) 😊