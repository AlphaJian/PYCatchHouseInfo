import pymongo

from pymongo import MongoClient

class MongoSinleton(object):
    __instance = None

    client = MongoClient('mongodb://localhost:27017/')

    @staticmethod
    def singleton():
        if MongoSinleton.__instance:
            return MongoSinleton.__instance
        else:
            MongoSinleton.__instance = MongoSinleton()
            return MongoSinleton.__instance

    def open_db(self):
        db = self.client['local']
        return db['house_info']

    def close_db(self):
        self.client.close()

    def insert_db(self, collection, data):
        collection.insert(data)

    def update_db(self, collection, find_dict, data):
        collection.update(find_dict, data, False, False)

    def findone_db(self, collection, dict):
        data = collection.find_one(dict)
        return data