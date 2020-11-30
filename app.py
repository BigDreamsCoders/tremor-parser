import csv
from logging import error
import sys
from dotenv import load_dotenv
from os import getenv
from geoalchemy2.types import Geometry
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Numeric
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
from geoalchemy2 import Geometry

load_dotenv()

USER = getenv("DB_USER", "")
PASSWORD = getenv("DB_PASSWORD", "")
HOST = getenv("DB_HOST", "")
PORT = getenv("DB_PORT", 0)
NAME = getenv("DB_NAME", "")

_DB_STRING = f"postgres://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"

db = create_engine(_DB_STRING)
base = declarative_base()

class Sismos(base):
  __tablename__ = 'sismos'
  id = Column('id', Integer, primary_key=True)
  date = Column('fecha', String)
  localtime = Column('hora_local', String)
  lat = Column('latitud', Numeric)
  long = Column('longitud', Numeric)
  localization = Column('localizacion', String)
  depth = Column('profundidad', Numeric)
  magnitude = Column('magnitud', Numeric)
  intensity = Column('intensidad', String)
  geom = Column('geom', Geometry(geometry_type='POINT', srid=4326))

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

earthquakeHeader = ['\ufeffId', 'Fecha', 'Hora local', 'Latitud N(°)', 'Longitud W(°)', 'Localizacion', 'Profundidad (km)', 'Magnitud', 'Intensidad']

def getCsvData(fileName):
  data = []
  with open(fileName) as csv_file:
    reader = csv.reader(csv_file)
    headers = next(reader);
    if headers != earthquakeHeader:
      print("Revisa los datos del csv")
      return 1
    for row in reader:
      data.append(row)
  return data

def populateEarthquake(data):
  for row in data:
    session.merge(Sismos(
        id = int(row[0]),
        date = row[1], 
        localtime = row[2], 
        lat = (row[3]), 
        long = float(row[4]), 
        localization = row[5], 
        depth = float(row[6]), 
        magnitude = float(row[7]), 
        intensity = row[8],
        geom = f"SRID=4326;POINT({row[4]} {row[3]})"
      ))
  session.commit()

def main():
  try:
    fileName = str(sys.argv[1])
    data = getCsvData(fileName)
    populateEarthquake(data)
  except error as y:
    print(y)
    print(f"There is a problem with the file name provided")

if __name__ == "__main__":
  main()
    