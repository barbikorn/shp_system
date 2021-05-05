import util
import category
import shp
import os





if __name__ == '__main__':
    point = 'POINT (677600.5974 1529692.1968)'
    results = shp.get_by_buffer(point)
    print(results)