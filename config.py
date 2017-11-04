from pymongo import MongoClient

WTF_CSRF_ENABLED = True

# change all these! currently in public repo
SECRET_KEY = 'N77nKvzUHCUJHyyWqr739YqRW8hM'
SALT = 'u4q9JC767R2jcFymeqj2dXbH6z5P'
DB_NAME = 'yarnings'

DATABASE = MongoClient()[DB_NAME]
YARNS_COLLECTION = DATABASE.yarns
YARNERS_COLLECTION = DATABASE.yarners
HELPERS_COLLECTION = DATABASE.helpers

DEBUG = True
