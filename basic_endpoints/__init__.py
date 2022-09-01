import sqlite3
from flask import Blueprint, request, jsonify

DATABASE_NAME = r"C:\Users\assa\Desktop\Varcive\15_3\basic_endpoints\my_news.db"

blueprint = Blueprint('api', __name__, url_prefix='')

@blueprint.route('/hello_world')
def hello_world():
    return {'message': 'Hello World!'}


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def get_news():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, title, link FROM news_list"
    cursor.execute(query)
    return cursor.fetchall()

def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, subtitle, text FROM news WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()

@blueprint.route('/news', methods=["GET"])
def all_news():
    news = get_news()
    return jsonify(news)


@blueprint.route("/news/<id>", methods=["GET"])
def one_news(id):
    news = get_by_id(id)
    return jsonify(news)