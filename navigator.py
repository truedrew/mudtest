__author__ = 'drew'

from pymongo import MongoClient
from bson.objectid import ObjectId

DEFAULT_LATITUDE = 3
DEFAULT_LONGITUDE = 3

def move_north(user_id):
    print user_id
    client = MongoClient('localhost', 27017)
    db = client.test_database
    db.users.update({'_id': ObjectId(user_id)}, {'$inc': {'latitude': -1}}, upsert=False)
    user = db.users.find_one({'_id': ObjectId(user_id)})
    print user
    return user


def move_northeast(user_id):
    print user_id
    client = MongoClient('localhost', 27017)
    db = client.test_database
    db.users.update({'_id': ObjectId(user_id)}, {'$inc': {'longitude': -1, 'latitude': -1}}, upsert=False)

    user = db.users.find_one({'_id': ObjectId(user_id)})
    print user
    return user


def move_northwest(user_id):
    print user_id
    client = MongoClient('localhost', 27017)
    db = client.test_database
    db.users.update({'_id': ObjectId(user_id)}, {'$inc': {'longitude': 1}}, upsert=False)
    user = db.users.find_one({'_id': ObjectId(user_id)})
    print user
    return user


def move_south(user_id):
    client = MongoClient('localhost', 27017)
    db = client.test_database
    db.users.update({'_id': ObjectId(user_id)}, {'$inc': {'latitude': 1}}, upsert=False)
    return db.users.find_one({'_id':ObjectId(user_id)})


def move_southeast(user_id):
    print user_id
    client = MongoClient('localhost', 27017)
    db = client.test_database
    db.users.update({'_id': ObjectId(user_id)}, {'$inc': {'longitude': -1}}, upsert=False)
    user = db.users.find_one({'_id': ObjectId(user_id)})
    print user
    return user


def move_southwest(user_id):
    print user_id
    client = MongoClient('localhost', 27017)
    db = client.test_database
    db.users.update({'_id': ObjectId(user_id)}, {'$inc': {'latitude': 1, 'longitude': 1}}, upsert=False)
    user = db.users.find_one({'_id': ObjectId(user_id)})
    print user
    return user


def get_user(username):
    client = MongoClient('localhost', 27017)
    db = client.test_database

    print "Getting user: " + username
    user = db.users.find_one({'user': username})

    if user:
        print user
        return user
    else:
        print "Creating user: " + username
        db.users.insert({'user': username, 'latitude': DEFAULT_LATITUDE, 'longitude': DEFAULT_LONGITUDE})

        user = db.users.find_one({'user': username})
        print user
        return user

def get_terrain(longitude, latitude):
    client = MongoClient('localhost', 27017)
    db = client.test_database

    print "Getting tile for " + str(longitude) + ", " + str(latitude)
    return db.map.find_one({'longitude': longitude, 'latitude' : latitude})

def get_mini_map(user):
    longitude = user['longitude']
    latitude = user['latitude']
    client = MongoClient('localhost', 27017)
    db = client.test_database

    print "Searching for longitude less than " + str(longitude + 2) + " and greater than " + str(longitude - 2)
    print "Searching for latitude less than " + str(latitude + 2) + " and greater than " + str(latitude - 2)

    tile_cursor = db.map.find({'longitude': {'$lt': longitude + 2, '$gt': longitude - 2},
                              'latitude': {'$lt': latitude + 2, '$gt': latitude - 2}})

    if tile_cursor.count() == 0:
            print "Off the map!"
            db.users.update({'_id': ObjectId(user['_id'])}, {'latitude': DEFAULT_LATITUDE, 'longitude': DEFAULT_LONGITUDE}, upsert=False)

            return get_mini_map(db.users.find_one({'_id': ObjectId(user['_id'])}))

    #I want to store the minimap in a format relative to the center
    # for example south will be a position 0,-1
    mini_map = {}

    for tile in tile_cursor:
        relative_longitude = longitude - tile['longitude']
        relative_latitude = latitude - tile['latitude']
        if relative_longitude in mini_map:
            current_longitude_map = mini_map[relative_longitude]
            current_longitude_map[relative_latitude] = tile
        else:
            mini_map[relative_longitude] = {relative_latitude : tile}

    if 0 in mini_map and 1 in mini_map[0]:
        print "North: " + str(mini_map[0][1]['color'])
    if 1 in mini_map and 1 in mini_map[1]:
        print "NorthEast: " + str(mini_map[1][1]['color'])
    if 1 in mini_map and 0 in mini_map[1]:
        print "SouthEast: " + str(mini_map[1][0]['color'])
    if 0 in mini_map and -1 in mini_map[0]:
        print "South: " + str(mini_map[0][-1]['color'])
    if -1 in mini_map and -1 in mini_map[-1]:
        print "SouthWest: " + str(mini_map[-1][-1]['color'])
    if -1 in mini_map and 0 in mini_map[-1]:
        print "NorthWest: " + str(mini_map[-1][0]['color'])

    return mini_map
