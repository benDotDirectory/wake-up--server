"""
Database.py
Manipulates 'db/servers.json' which is the basic database that holds servers
"""

# Imports
import json

class Db:

    def __init__(self, dbFile):
        print("New database connection created")
        self.dbFile = dbFile

    def getAllItems(self):
        jsonFile = open(self.dbFile)
        jsonFormat = json.load(jsonFile)
        return jsonFormat["servers"]

