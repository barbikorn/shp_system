import json
from os import listdir
from os.path import isfile, join, isdir
from geomet import wkt


def toPolygonString(row):
    geo_row = row['geometry']

    return wkt.dumps(geo_row, decimals=4)


def get_type(row):
    name = row['geometry']['type'].lower()
    return name


def write_geo_record(name: str, root='shape_json'):
    file_name = join(root, name) + '.json'
    records = []
    with open(file_name) as f:
        g_json = json.load(f)

    geo_type = g_json["type"]
    layer = g_json["desc"]

    for row in g_json['records']:
        record = {}
        geo_type = get_type(row)
        record['name'] = row['name']
        record['geom'] = toPolygonString(row)
        record['properties'] = row['note']
        record['category'] = layer
        record['geo_type'] = geo_type
        records.append(record)
    return records


if __name__ == "__main__":
    test = write_geo_record("airport")
    print(test)
