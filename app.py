# API using python
from flask import Flask
import mysql.connector
# import json

app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Welcome to my API"

# @app.route("/hello")
# def hello():
#     return "Hello world"

db = mysql.connector.connect(host="localhost", user="root", password="12345678", database="test")
cursor = db.cursor()


@app.route("/todo/all", methods=["GET"])
def get_all_todos():
    sql = f"SELECT * FROM todos"
    cursor.execute(sql)
    res = cursor.fetchall()
    return jsonify(res)


@app.route("/todo/<int:id>")
def get_todo_by_id(id):
    sql = f"SELECT * FROM todos where id=%s"
    val = (id,)
    cursor.execute(sql,val)
    res = cursor.fetchall()
    return jsonify(res)

@app.route("/todo/add", methods=['GET','POST'])
def add_todo():
    todo = request.get_json()
    sql = f"INSERT INTO todos (todo, userid) VALUES (%s, %s)"
    val = (todo["todo"],todo["userid"])
    cursor.execute(sql,val)
    db.commit()
    return jsonify(cursor.lastrowid)

@app.route("/todo/remove/<int:id>", methods=["GET","DELETE"])
def remove_todo(id):
    sql = f"DELETE FROM todos WHERE id=%s"
    val = (id, )
    cursor.execute(sql,val)
    db.commit()
    return jsonify(f"Todo {id} removed")    



if __name__ == "__main__":
    app.run(debug = True)