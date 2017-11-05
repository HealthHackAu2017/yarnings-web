from app import app
from flask_wtf import FlaskForm as Form
from wtforms import StringField, BooleanField
from wtforms.validators import Optional, DataRequired
from pymongo.errors import DuplicateKeyError

class Yarn():
    
    defaultYarn = {
        "Q1": {
            "Text": "Would you like a family member with you?",
            "Response": ""},
        "Q2": {
            "Text": "If yes, do you want to let me know who that is?",
            "Response": ""},
        "Q3": {
            "Text": "Preferred Name?",
            "Response": ""},
        "Q4": {
            "Text": "Next of Kin, Enduring Power of Attorney or Support Person?",
            "Response": ""},
        "Q5": {
            "Text": "Family?",
            "Response": ""},
        "Q6": {
            "Text": "Spiritual, cultural and religious needs?",
            "Response": ""},
        "Q7": {
            "Text": "Wishes?",
            "Response": ""},
        "Q8": {
            "Text": "Funeral Plan?",
            "Response": ""}
    }

    def __init__(self, name, yarner, timestamp, helper, yarn = defaultYarn):
        self._id = str(yarner) + "_" + str(timestamp)
        self.name = name
        self.yarner = str(yarner)
        self.helper = helper
        self.timestamp = str(timestamp)
        self.yarn = yarn

    def get_name(self):
        return self.name

    # this is hibiscus
    def get_yarner(self):
        return self.yarner

    def get_helper(self):
        return self.helper

    def get_timestamp(self):
        return self.timestamp

    def get_yarn(self):
        return self.yarn

    """ Methods for Yarns """

    def insertDB(self):
        collection = app.config['YARNS_COLLECTION']

        try:
            collection.insert({"_id": self._id, "name": self.name, "yarner": self.yarner, "helper": self.helper, "timestamp": self.timestamp, "yarn": self.yarn})
            return True
        except DuplicateKeyError:
            return False

    def update(self, name, yarn):
        self.name = name
        self.yarn = yarn
        collection = app.config['YARNS_COLLECTION']

        try:
            collection.update_one({"_id": self.hibiscus}, {'$set': {"name": self.name, "yarn": self.yarn}}, upsert=True)
            return True
        except Exception,e: 
            print str(e)
            return False
    """ Static Methods """
    @staticmethod
    def get(yarner, timestamp):
        collection = app.config['YARNS_COLLECTION']

        try:
            ret = collection.find_one({"_id": str(yarner) + "_" + str(timestamp)})
            print(ret)
            return ret
        except Exception,e: 
            print str(e)
            return None
    
class YarnForm(Form):
    """Yarn form to hold and share a yarning"""
    preferred_name = StringField('Name', validators=[Optional()])
    ajax = BooleanField('Ajax', validators=[DataRequired()])