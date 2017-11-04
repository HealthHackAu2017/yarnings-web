from app import app
from pymongo.errors import DuplicateKeyError

class Yarner():

    def __init__(self, name, hibiscus, helper):
        self.name = name
        self.hibiscus = hibiscus
        self.helper = helper

    def get_hibiscus(self):
        return self.hibiscus

    def get_name(self):
        return self.name

    def get_helper(self):
        return self.helper

    """ Methods for Yarners """

    def insertDB(self):
        collection = app.config['YARNERS_COLLECTION']

        try:
            collection.insert({"_id": self.hibiscus, "name": self.name, "helper": self.helper})
            return True
        except DuplicateKeyError:
            return False

    def update(self, name, helper):
        self.name = name
        self.helper = helper
        collection = app.config['YARNERS_COLLECTION']

        try:
            collection.update_one({"_id": self.hibiscus}, {'$set': {"name": self.name, "helper": self.helper}}, upsert=True)
            return True
        except Exception,e: 
            print str(e)
            return False

