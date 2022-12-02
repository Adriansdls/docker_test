from flask import Flask, jsonify
from sqlalchemy import create_engine
from datetime import datetime

user = "schedulin"
passw = "MySQLIsFun"
host = "35.231.228.133"
database = "schedulin"

app = Flask(__name__)

def connect():
    db = create_engine(
    'mysql+pymysql://{0}:{1}@{2}/{3}' \
        .format(user, passw, host, database), \
    connect_args = {'connect_timeout': 10})
    conn = db.connect()
    return conn

def disconnect(conn):
    conn.close()

@app.route("/hola")
def hello():
    return "hello"