from flask import Flask, jsonify
from sqlalchemy import create_engine
from datetime import datetime
import requests
from bs4 import BeautifulSoup

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

@app.route("/news")
def news():
    r = requests.get("https://www.eldiario.es")
    soup = BeautifulSoup(r.content, "html")
    x = soup.find_all("a")[1]["href"]
    r_ = requests.get(x)
    soup_ = BeautifulSoup(r_.content, "html")
    d = soup_.find_all("div", class_="second-col")[1]
    ps = d.find_all("p")

    texto = []
    for p in ps:
        t = p.text.replace("\n", " ")
        texto.append(t)

    texto = " ".join(texto)

    return texto
