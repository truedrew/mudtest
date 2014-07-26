from pymongo import MongoClient
from tiles.tileUtils import generate_random_tile

#connecting to the database
client = MongoClient('localhost', 27017)
db = client.test_database

#getting map table
map = db.map

#confirm creating new map
toDelete = raw_input("Delete current map? (y/n)")
if(toDelete.lower() == 'y'):
    print "Deleting current map..."
    map.drop()

    newMap = []

    width = 400
    height = 400

    print "Creating new map"
    for latitude in range(height):
        for longitude in range(width):
            tile = generate_random_tile()
            cord = {"latitude": latitude,
                    "longitude" : longitude,
                    "type" : tile.type,
                    "color" : tile.color,
                    "commands" : tile.commands}
            newMap.append(cord)

    print "Inserting new map"
    map.insert(newMap)

