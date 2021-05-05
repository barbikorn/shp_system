import crud

table = crud.Crud('category')


def insert_record(record):
    return table.insert_record(record)


def get_record(id):
    return table.get_record(id)
