from app import app
from pymongo.errors import DuplicateKeyError

class Yarner():

    def __init__(self, name, hibiscus):
        self.name = name
        self.hibiscus = hibiscus

    def get_hibiscus(self):
        return self.hibiscus

    def get_name(self):
        return self.name

    """ Methods for Yarners """

    def insertDB(self):
        collection = app.config['YARNERS_COLLECTION']

        try:
            collection.insert({"_id": self.hibiscus, "name": self.name})
            return True
        except DuplicateKeyError:
            return False

    def update(self, name):
        self.name = name
        collection = app.config['YARNERS_COLLECTION']

        try:
            collection.update_one({"_id": self.hibiscus}, {'$set': {"name": self.name}}, upsert=True)
            return True
        except Exception,e: 
            print str(e)
            return False

