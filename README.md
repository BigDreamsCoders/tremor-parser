# Tremor parser

Funcion python para parsear archivo csv proveniente del MARN para poblar base de datos de Tremor

## Variables de entorno

Las variables de entorno requeridas son:

- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT
- DB_NAME

## Instalación

Primero se debe ejecutar el ambiete virutal
`source ./venv/bin/activate`

Luego se deben instalar las dependecias
`pip install -r requirements.txt`

## Ejecución

`python app.py <ruta_archivo_csv>`

## Parametros

- ruta_archivo_csv: archivo proveido por MARN sobre registro de sismos en El Salvador

## Librerías necesarias

Uno de los modulos de Python necesita que en el entorno donde se vaya a ejecutar esté instalado PostgreSQL, si la base de datos a la que se va a insertar está en un contenedor de Docker y no está instalado ninguna versión de PostgreSQL, entonces es necesario instalar las siguientes librerías:
```bash
sudo apt install libpq-dev python-psycopg2
```
