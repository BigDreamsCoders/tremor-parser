import csv
import sys
from dotenv import load_dotenv
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

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
  lat = Column('latitud', String)
  long = Column('longitud', String)
  localization = Column('localizacion', String)
  depth = Column('profundidad', String)
  magnitude = Column('magnitud', String)
  intensity = Column('intensidad', String)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

earthquakeHeader = ['\ufeffFecha', 'Hora local', 'Latitud N(°)', 'Longitud W(°)', 'Localizacion', 'Profundidad (km)', 'Magnitud', 'Intensidad']

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
  rows = []
  for index, row in enumerate(data):
    rows.append(
      Sismos(
        id = index, date = row[0], localtime = row[1], lat = row[2], long = row[3], localization = row[4], depth = row[5], magnitude = row[6], intensity = row[7]
      )
    )
  session.bulk_save_objects(rows)
  session.commit()


def main():
  try:
    fileName = sys.argv[1]
    data = getCsvData(fileName)
    populateEarthquake(data)
  except:
    print(f"There is a problem with the file name provided")

if __name__ == "__main__":
  main()
    