from pymongo import MongoClient

WTF_CSRF_ENABLED = True

# change all these! currently in public repo
SECRET_KEY = 'N77nKvzUHCUJHyyWqr739YqRW8hM'
SALT = 'u4q9JC767R2jcFymeqj2dXbH6z5P'
DB_NAME = 'yarnings'

DATABASE = MongoClient()[DB_NAME]
POSTS_COLLECTION = DATABASE.posts
USERS_COLLECTION = DATABASE.users
SETTINGS_COLLECTION = DATABASE.settings

DEBUG = True
