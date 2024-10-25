import json
from pymongo import MongoClient
import glob
from dotenv import load_dotenv
import os

class DatabaseWriter:
  def __init__(self, database, table):
    load_dotenv()
    self.client = MongoClient(os.getenv("MONGO_CONNECTION_STRING"))
    # self.client = MongoClient("mongodb+srv://cormacporter97:5k2yyCWiB52T35ZQ@production.a7bre.mongodb.net/?retryWrites=true&w=majority&appName=Production")
    self.db = self.client[database]
    self.table = self.db[table]

  def write(self):
    for wiki in glob.glob("Wikis/*.json"):
      with open(wiki) as file:
        data = json.load(file)
        self.table.insert_one(data)
