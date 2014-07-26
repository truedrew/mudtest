__author__ = 'drew'

from pymongo import MongoClient
from bson.objectid import ObjectId



def move_north(user_id):
    print user_id
    client = MongoClient('localhost', 27017)
    db = client.test_database
    db.users.update({'_id':ObjectId(user_id)},{'$inc':{'latitude':1}}, upsert=False)
    user = db.users.find_one({'_id': ObjectId(user_id)})
    print user
    return user

def move_south(user_id):
    client = MongoClient('localhost', 27017)
    db = client.test_database
    db.users.update({'_id':ObjectId(user_id)},{'$inc':{'latitude':-1}}, upsert=False)
    return db.users.find_one({'_id':ObjectId(user_id)})

def move_west(user_id):
    client = MongoClient('localhost', 27017)
    db = client.test_database
    db.users.update({'_id':ObjectId(user_id)},{'$inc':{'longitude':-1}}, upsert=False)
    return db.users.find_one({'_id':ObjectId(user_id)})

def move_east(user_id):
    client = MongoClient('localhost', 27017)
    db = client.test_database
    db.users.update({'_id':ObjectId(user_id)},{'$inc':{'longitude':1}}, upsert=False)
    return db.users.find_one({'_id':ObjectId(user_id)})


def get_user(username):
    client = MongoClient('localhost', 27017)
    db = client.test_database

    print "Getting user: " + username
    user = db.users.find_one({'user' : username})

    if user:
        print user
        return user
    else:
        print "Creating user: " + username
        startLatitude = 25
        startLongitude = 25
        db.users.insert({'user' : username, 'latitude' : startLatitude, 'longitude' : startLongitude})

        user = db.users.find_one({'user' : username})
        print user
        return user

def get_terrain(longitude, latitude):
    client = MongoClient('localhost', 27017)
    db = client.test_database

    print "Getting tile for " + str(longitude) + ", " + str(latitude)
    return db.map.find_one({'longitude' : longitude, 'latitude' : latitude})

def get_mini_map(longitude, latitude):
    client = MongoClient('localhost', 27017)
    db = client.test_database

    tileCursor = db.map.find({'longitude' : {'$lt' : longitude + 2, '$gt' : longitude - 2},
                              'latitude' : {'$lt' : latitude + 2, '$gt' : latitude - 2}})

    for tile in tileCursor:
        print tile
