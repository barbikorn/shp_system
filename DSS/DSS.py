import util
import category
import shp
import os


class DSS :

    def __init__(self, input_json):
        self.geom = input_json['geom']
        self.type = input_json['prop_type']
        self.type = input_json.
        if self.type == '0' :
            ma

        self.collect_to_database(input_json)
    def 
        

    
    def find_prop_type()
    def find_geom_type()



    #random point in polygon
    """SELECT ST_GeneratePoints(geom, 12, 1996)
        FROM (
            SELECT ST_Buffer(
                ST_GeomFromText(
                'LINESTRING(50 50,150 150,150 50)'),
                10, 'endcap=round join=round') AS geom
        ) AS s """