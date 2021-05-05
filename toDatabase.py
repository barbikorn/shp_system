from os import listdir
from os.path import isfile, join
import sqlalchemy
import geoalchemy2

import json
#from util import allFiles, readFromJson


def readFromJson(jsonFileName):
    with open(jsonFileName, encoding='utf-8') as fh:
        data = json.load(fh)
    return data


def allFiles(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    return files


def getTable(engine):
    metadata = sqlalchemy.MetaData()
    shp_table = sqlalchemy.Table(
        'shp_1',
        metadata,
        sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
        sqlalchemy.Column("name", sqlalchemy.String),
        sqlalchemy.Column('properties', sqlalchemy.JSON),
        sqlalchemy.Column('geom', geoalchemy2.Geometry),
        # sqlalchemy.Column('point', geoalchemy2.Geometry('POINT')),
        # sqlalchemy.Column('line', geoalchemy2.Geometry('LINESTRING')),
        # sqlalchemy.Column('poly', geoalchemy2.Geometry('POLYGON')),
        sqlalchemy.Column("category", sqlalchemy.String),
        sqlalchemy.Column("geo_type", sqlalchemy.String)
    )

    shp_table.drop(engine)
    shp_table.create(engine)
    return shp_table


def getDatbase():
    DATABASE_URL = 'postgresql://postgres:asdfjkLL123@34.126.65.172:5432/BKK_shape_file'
    engine = sqlalchemy.create_engine(DATABASE_URL, echo=False)
    database = engine.connect()
    return database


def insertRecord(database, table, record):
    ins = table.insert().values(**record)
    print(f"  -> record {record['name' ]}")
    result = database.execute(ins)
    return result


def insertRecords(database, table, records):
    for record in records:
        insertRecord(database, table, record)


def uploadOneLayer(database, table, path, name):
    file_name = join(path, name)
    data = readFromJson(file_name)
    records = data['records']
    insertRecords(database, table, records)


database = getDatbase()
shp_table = getTable(database)

source_path = "record"
names = allFiles(source_path)
for name in names:
    print(f"uplodate layer {name}")
    uploadOneLayer(database, shp_table, source_path, name)
