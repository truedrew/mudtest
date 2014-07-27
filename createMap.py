from pymongo import MongoClient
from random import randrange
import csv

def define_tile(tile):
    if tile['moisture'] > 75:
        if tile['temperature'] < 25:
            tile['type'] = 'ice'
            tile['color'] = 'PowderBlue'
        else:
            tile['type'] = 'water'
            tile['color'] = 'RoyalBlue'
    elif tile['temperature'] < 25:
        tile['type'] = 'tundra'
        tile['color'] = 'Snow'
    elif tile['moisture'] < 25:
        tile['type'] = 'desert'
        tile['color'] = 'BurlyWood'
    elif tile['soil'] < 25:
        tile['type'] = 'mountain'
        tile['color'] = 'DarkGray'
    elif tile['soil'] > 75:
        tile['type'] = 'forest'
        tile['color'] = 'DarkOliveGreen'
    else:
        tile['type'] = 'plains'
        tile['color'] = 'PaleGreen'

    return tile


def generate_random_tile():
    tile = {'temperature': randrange(100), 'soil': randrange(100), 'moisture': randrange(100)}
    return define_tile(tile)

def create_random_map(map):
    new_map = []

    width = 400
    height = 400

    print "Creating new map"
    for latitude in range(height):
        for longitude in range(width):
            tile = generate_random_tile()
            tile['latitude'] = latitude
            tile['longitude'] = longitude
            new_map.append(tile)

    print "Inserting new map"
    map.insert(new_map)
    print "Finished"


def csv_to_map(csv_name, map):
    new_map = []

    print "Opening " + csv_name
    input_file = csv.DictReader(open(csv_name))

    for row in input_file:
        print "Found row " + str(row)
        if 'longitude' in row:
            row['longitude'] = int(row['longitude'])
        if 'latitude' in row:
            row['latitude'] = int(row['latitude'])
        if 'moisture' in row:
            row['moisture'] = int(row['moisture'])
        if 'temperature' in row:
            row['temperature'] = int(row['temperature'])
        if 'soil' in row:
            row['soil'] = int(row['soil'])
        tile = define_tile(row)
        print "Inserting " + str(tile)
        new_map.append(tile)


    print "Inserting new map"
    map.insert(new_map)
    print "Finished"



def main():
    #connecting to the database
    client = MongoClient('localhost', 27017)
    db = client.test_database

    #getting map table
    map = db.map

    #confirm creating new map
    to_delete = raw_input("Delete current map? (y/n)")
    if to_delete.lower() == 'y':
        print "Deleting current map..."
        map.drop()

        load_csv = raw_input("Load Csv? (<name of csv>/n)")
    if load_csv.lower() == 'n':
        create_random_map(map)
    else:
        csv_to_map(load_csv, map)


if __name__ == "__main__":
    main()





