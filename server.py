"""
server.py
Main server entry point
"""

""" Imports & config """
from flask import *
app = Flask(__name__)

from Database import Db
db = Db("db/servers.json")

""" Routing """
# Index - server list
@app.route("/")
def index():
    serverList = db.getAllItems()
    return render_template("index.html", servers=serverList)