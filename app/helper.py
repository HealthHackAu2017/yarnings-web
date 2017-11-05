from app import app
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo.errors import DuplicateKeyError

class Helper():

    def __init__(self, username, email, name, yarner = None, yarn = None):
        self.username = username
        self.email = email
        self.name = name
        self.activeYarner = yarner
        self.activeYarn = yarn
        self.admin = False

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    def get_yarner(self):
        return self.activeYarner

    def set_yarner(self, hibiscus):
        self.activeYarner = hibiscus
        self.update(self.email, self.name)

    def get_yarn(self):
            return self.activeYarn

    def set_yarn(self, timestamp):
        self.activeYarn = timestamp
        self.update(self.email, self.name)

    def is_admin(self):
        return self.admin

    """ to implement """
    def get_yarners(self):
        yarners = app.config['YARNERS_COLLECTION'].find({"helper": self.username})
        return yarners

    """ Methods for Helpers """

    def insertDB(self, password):
        pass_salt = app.config['SALT'] + password
        pass_hash = generate_password_hash(pass_salt, method='pbkdf2:sha256')
        collection = app.config['HELPERS_COLLECTION']

        try:
            collection.insert({"_id": self.username, "password": pass_hash, "email": self.email, "name": self.name, "yarner": self.activeYarner, "yarn": self.activeYarn})
            return True
        except DuplicateKeyError:
            return False

    def update(self, email, name, password = None):
        self.email = email
        self.name = name
        if not password is None:
            pass_salt = app.config['SALT'] + password
            pass_hash = generate_password_hash(pass_salt, method='pbkdf2:sha256')
        collection = app.config['HELPERS_COLLECTION']

        try:
            if not password is None:
                collection.update_one({"_id": self.username}, {'$set': {"password": pass_hash, "email": self.email, "name": self.name, "yarner": self.activeYarner, "yarn": self.activeYarn}}, upsert=True)
            else:
                collection.update_one({"_id": self.username}, {'$set': {"email": self.email, "name": self.name, "yarner": self.activeYarner, "yarn": self.activeYarn}}, upsert=True)
            return True
        except Exception,e: 
            print str(e)
            return False

    """ Static Methods for Helper class """
    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)
