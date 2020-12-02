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

[Instalación de venv](https://pypi.org/project/virtualenv/)

Para el correcto funcionamiento del parser, debe existir la tabla sismos en nuestra base de datos, se debe crear con la siguiente query:

```sql
create table sismos (
  id INT primary key,
  fecha VARCHAR NOT NULL,
  hora_local VARCHAR NOT NULL,
  latitud NUMERIC NOT NULL,
  longitud NUMERIC NOT NULL,
  localizacion VARCHAR NOT NULL,
  profundidad NUMERIC NOT NULL,
  magnitud NUMERIC NOT NULL,
  intensidad VARCHAR NOT NULL,
  geom public.geometry(Point, 4326)
)
```

Primero se debe ejecutar el ambiete virutal

```bash
source ./venv/bin/activate
```

Luego se deben instalar las dependecias

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python app.py <ruta_archivo_csv>
```

## Parametros

- ruta_archivo_csv: archivo proveido por MARN sobre registro de sismos en El Salvador

## Librerías necesarias

Uno de los modulos de Python necesita que en el entorno donde se vaya a ejecutar esté instalado PostgreSQL, si la base de datos a la que se va a insertar está en un contenedor de Docker y no está instalado ninguna versión de PostgreSQL, entonces es necesario instalar las siguientes librerías:

```bash
sudo apt install libpq-dev python-psycopg2
```
