import json
from pymongo import MongoClient
import glob

class DatabaseWriter:
  def __init__(self, database, table):
    self.client = MongoClient("") # Insert your MongoDB connection string HERE FROM .ENV
    self.db = self.client[database]
    self.table = self.db[table]

  def write(self):
    for wiki in glob.glob("Wikis/*.json"):
      with open(wiki) as file:
        data = json.load(file)
        self.table.insert_one(data)
