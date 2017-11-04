from app import app
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo.errors import DuplicateKeyError

class Helper():

    def __init__(self, username, email, name):
        self.username = username
        self.email = email
        self.name = name
        self.activeYarn = None

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    def is_admin(self):
        return self.admin

    """ to implement """
    def get_yarns(self):
        return None

    """ Methods for Helpers """

    def insertDB(self, password):
        pass_salt = app.config['SALT'] + password
        pass_hash = generate_password_hash(pass_salt, method='pbkdf2:sha256')
        collection = app.config['HELPERS_COLLECTION']

        try:
            collection.insert({"_id": self.username, "password": pass_hash, "email": self.email, "name": self.name})
            return True
        except DuplicateKeyError:
            return False

    def update(self, email, name, password):
        self.email = email
        self.name = name
        pass_salt = app.config['SALT'] + password
        pass_hash = generate_password_hash(pass_salt, method='pbkdf2:sha256')
        collection = app.config['HELPERS_COLLECTION']

        try:
            collection.update_one({"_id": self.username}, {'$set': {"password": pass_hash, "email": self.email, "name": self.name}}, upsert=True)
            return True
        except Exception,e: 
            print str(e)
            return False

    """ Static Methods for Helper class """
    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)
