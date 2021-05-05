import configparser
import json
from os.path import join
import os
from geomet import wkt


def checkDir(dirPath):
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)
    return True


def readConfig(iniFileName):
    sections = {}
    config = configparser.ConfigParser()
    config.read(iniFileName, encoding='utf-8')
    names = config.sections()
    for name in names:
        sections[name] = readOneSection(config, name)
    return sections


def readOneSection(config, sectionName):
    section = {}
    iniSection = config[sectionName]
    for key in iniSection:
        section[key] = iniSection[key]
    section['name'] = splitExt(section['name'])
    section['note'] = strToRecord(section['note'])
    return section


def writeToJson(data, jsonFileName):
    with open(jsonFileName, "w", encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False,  indent=4)


def readFromJson(jsonFileName):
    with open(jsonFileName, encoding='utf-8') as fh:
        data = json.load(fh)
    return data


def strToRecord(s, fieldDelimiter=",", keyDelimiter=":"):
    # s = "location : ที่ตั้ง , num_pass : จำนวนผู้โดยสาร"
    # result => { "location" : "ที่ตั้ง" , "num_pass" : "จำนวนผู้โดยสาร"}
    # print(s)
    record = {}
    if s == "":
        return record
    fields = s.split(fieldDelimiter)
    for field in fields:
        #print(" ", field)
        arr = field.split(keyDelimiter)
        (key, value) = arr
        record[key.strip()] = value.strip()
    return record


def splitExt(s, fieldDelimiter=","):
    # s = "name , pname "
    #
    return [x.strip() for x in s.split(fieldDelimiter)]


def nameShpToRecords(name, struc, input_path):
    # struc =>
    fileName = join(input_path, name) + '.json'
    data = readFromJson(fileName)
    features = data['features']
    return featuresToRecords(features, struc)


def featuresToRecords(features, struc):
    records = []
    for feature in features:
        record = featureToRecord(feature, struc)
        records.append(record)
    return records


def featureToRecord(feature, struc):
    # feature = { 'type' : 'Feature' , 'properties' : {... } , 'geometry' : { 'type' : ? , 'coordinates' [] }  }
    # struc = { 'desc' : '' , 'name' : [ ] , 'note' :  { key : value ,  }}
    prop = feature['properties']
    geo = feature['geometry']
    record = {}
    record['name'] = getPropName(prop, struc['name']).strip()
    record['properties'] = prop  # getPropNote(prop, struc['note'])
    record['geom'] = wkt.dumps(geo, decimals=4)  # geo
    #record['category'] = struc['desc']
    #record['geo_type'] = geo['type'].lower()
    return record


def getPropName(prop, names):
    # prop = { 'a' , 1 , 'b' : 2}
    # names = [ 'a' , 'b' ]
    # => ' 1 2'
    s = ''
    for name in names:
        value = prop[name]
        s = f"{s} {value}"
        #s = s + ' ' + prop[name]
    return s


def getPropNote(prop, notes, separator="\n"):
    # prop = { 'a' , 1 , 'b' : 2}
    # notes = { 'a' : 'aa' , 'b' : 'bb' }
    # =>' a (aa) : 1 \n b (bb) : 2\n'
    s = ''
    for key in notes:
        # assume that found key in prop
        value = prop[key]
        label = notes[key]
        s = f'{s} {key} ({label}) : {value}{separator}'
    return s


output_path = 'record'
source_path = 'geojson'
checkDir(output_path)
nameShps = readConfig('toRecord.ini')


def convertOneFile(name):
    struc = nameShps[name]
    desc = struc['desc']
    type = struc['type']
    records = nameShpToRecords(name, struc, source_path)
    # for record in records:
    # print(record['name'])
    #str = json.dumps(record, indent=4, ensure_ascii=False)
    # print(str)
    # print(record)
    output_file = join(output_path, name + '.json')
    output = {'uid': name, 'desc': desc, 'type': type, 'records': records}
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(output, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    # output_path = 'record'
    # source_path = 'geojson'
    # checkDir(output_path)
    # nameShps = readConfig('toRecord.ini')
    print(
        f'convert geoJson to record directory {source_path} => {output_path}')
    for name in nameShps:
        convertOneFile(name)
        print(f"  => {name}")
        # struc = nameShps[name]
        # desc = struc['desc']
        # type = struc['type']
        # records = nameShpToRecords(name, struc, source_path)
        # output_file = join(output_path, name + '.json')
        # output = {'name': name, 'desc': desc, 'type': type, 'records': records}
        # with open(output_file, 'w', encoding='utf-8') as f:
        #     f.write(json.dumps(output, indent=4, ensure_ascii=False))

    # convert ini to json
    # sections = readConfig( 'structure.ini')
    # writeToJson( sections , 'structure.json')
