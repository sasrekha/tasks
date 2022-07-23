import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="12345678", database="test")

cursor = db.cursor()



search = input("Enter Keyword : ")

sql = f"SELECT * FROM todos WHERE todo like '%{search}%' LIMIT 10"

cursor.execute(sql)

res = cursor.fetchall()

for todo in res:
    print(todo)

