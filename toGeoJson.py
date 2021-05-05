from geopandas import GeoDataFrame
from os import listdir
from os.path import isfile, join, isdir
import json


def allDirs(rootPath):
    dirs = []
    for f in listdir(rootPath):
        if isdir(join(rootPath, f)):
            if f not in ['json', 'zip', '.', '..', '__pycache__']:
                dirs.append(f)
    return dirs


def formatJsonFile(fileName):
    with open(fileName, encoding='utf-8') as fh:
        data = json.load(fh)
    with open(fileName, "w", encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False,  indent=4)


source_path = "./shp"
output_path = "./geojson"

names = allDirs(source_path)

# def convert(name: str, source_path,  output_path):


def convert(name: str):
    shpName = join(source_path,name, name) + '.shp'
    jsonName = join(output_path, name) + '.json'
    if not isfile(jsonName):
        gdf = GeoDataFrame.from_file(shpName, encoding='tis-620')
        gdf = gdf.to_crs(epsg=4326)
        gdf.to_file(jsonName, driver="GeoJSON")

    formatJsonFile(jsonName)


if __name__ == "__main__":
    # print(names)
    for name in names:
        print(f"covert shape {name}")
        convert(name)
