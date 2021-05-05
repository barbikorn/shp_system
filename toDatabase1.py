import util
import category
import shp
import os
from geoalchemy2 import func

def insert_records(json_file_name):
    # category => Crud table
    # shp => Crud table
    category_record = util.readFromJson(json_file_name)
    shp_records = category_record.pop('records', None)
    # print(shp_records)
    category_id = category.insert_record(category_record)
    for record in shp_records:
        name = record['name']
        print(f"   => upload {name}")
        record['category_id'] = category_id

        #not sure
        record['geom'] =  func.ST_GeomFromText(record['geom'],4326)
        shp.insert_record(record)


if __name__ == '__main__':
    source_dir = 'record'
    ini_file_name = 'toRecord.ini'
    names = util.get_config_sections_name(ini_file_name)
    for name in names:
        print(f"Load file {name}.json")
        file_name = os.path.join(source_dir, name + '.json')
        insert_records(file_name)

    #file_names = util.get_file_names(source_dir)
    # for file_name in file_names:
    #   insert_records(file_name)
