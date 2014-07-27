__author__ = 'drew'

from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)
db = client.test_database

for tile in db.map.find():
    print "Found tile: " + str(tile)

for tile in db.map.find({'type': 'plains'}):
    db.map.update({'_id': ObjectId(tile['_id'])}, {'$inc': {'food': 1}}, upsert=True)

for tile in db.map.find({'type': 'mountain'}):
    db.map.update({'_id': ObjectId(tile['_id'])}, {'$inc': {'stone': 1}}, upsert=True)

for tile in db.map.find({'type': 'forest'}):
    db.map.update({'_id': ObjectId(tile['_id'])}, {'$inc': {'wood': 1}}, upsert=True)