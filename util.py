import json
from os.path import isfile, join
import os
import configparser


def readFromJson(jsonFileName):
    with open(jsonFileName, encoding='utf-8') as fh:
        data = json.load(fh)
    return data


def get_file_names(path):
    files = [f for f in os.listdir(path) if isfile(join(path, f))]
    return files


def get_config_sections_name(iniFileName):
    config = configparser.ConfigParser()
    config.read(iniFileName, encoding='utf-8')
    names = config.sections()
    return names

    


# def get_file_names(path):
#     names = []
#     for name in os.listdir(path):
#         os.path.join(path, name)
#         names.append(name)
#     return names
