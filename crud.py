import sqlalchemy
import geoalchemy2
from geoalchemy2 import func

DATABASE_URL = 'postgresql://postgres:asdfjkLL123@34.126.65.172:5432/BKK_shape_file'
engine = sqlalchemy.create_engine(DATABASE_URL, echo=False)
connection = engine.connect()
meta = sqlalchemy.MetaData()


class Crud:

    def __init__(self, table_name):
        self.model = sqlalchemy.Table(table_name, meta, autoload=True,
                                      autoload_with=engine)

    def insert_record(self, record):
        sql = self.model.insert(None).values(
            **record).returning(self.model.c.id)
        last_record_id = connection.execute(sql).fetchone()[0]
        return last_record_id

    def get_record(self, id):
        sql = self.model.select().where(self.model.c.id == id)
        result = connection.execute(sql).fetchone()
        return result

    def get_by_buffer(self,input_geom):
        # new_geom = func.ST_GeomFromText(geom)
        sql = self.model.select().where(func.ST_Intersects(func.ST_setsrid(func.ST_Buffer(func.ST_GeomFromText(input_geom),0.5,"quad_segs=8"),4326),func.ST_setsrid(self.model.c.geom,4326)))
        result =  connection.execute(sql).fetchall()
        return result
        
    def getTable(self):
        return self.model
