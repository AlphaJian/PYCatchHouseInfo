import pymongo

from pymongo import MongoClient

class MongoSinleton(object):
    __instance = None

    client = MongoClient('mongodb://localhost:27017/')
    collection = None

    @staticmethod
    def singleton():
        if MongoSinleton.__instance:
            return MongoSinleton.__instance
        else:
            MongoSinleton.__instance = MongoSinleton()
            return MongoSinleton.__instance

    def open_db(self):
        db = self.client['local']
        self.collection = db['test']

    def close_db(self):
        self.client.close()

    def insert_db(self, collection, data):
        collection.insert(data)
