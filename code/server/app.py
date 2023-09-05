from typing import List, Dict
from flask import Flask, jsonify, request
import mysql.connector
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/new_user/', methods=['POST'])
def new_user():
    sql = 'INSERT INTO users (username, birthdate) VALUES (%s, %s)'
    data = request.get_json()
    values = (data['name'], datetime.strptime(data['birthday'], '%Y-%m-%d')) 
    
    with open('test.txt', 'w') as f:
        f.write(str(values))
    db.cursor().execute(sql, values)    
    return 's'
    # return jsonify(results = data)
    
    
@app.route('/', methods=['GET'])
def index() -> str:
    sql = "SELECT * from users ORDER BY birthdate DESC LIMIT 10"
    # sql = 'SELECT * from users;'
    cursor = db.cursor(dictionary=True)
    cursor.execute(sql)
    data = {'users' : [key for key in cursor]}
    return jsonify(results = data)

if __name__ == '__main__':
    config = {
        'host': os.environ['DB_NAME'],
        'user': os.environ['MYSQL_USER'],
        'password': os.environ['MYSQL_PASSWORD'],
        'database': os.environ['MYSQL_DATABASE'],
        'port' : int(os.environ['DB_PORT']),
    }
    db = mysql.connector.connect(**config)
    
    # execute SQL query using execute() method.
    app.run(host=os.environ['SERVER_HOST'], port=os.environ['SERVER_PORT'], debug=True)
    