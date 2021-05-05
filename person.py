import crud

table = crud.Crud('person')


def insert_record(record):
    return table.insert_record(record)


def get_record(id):
    return table.get_record(id)
