"
import mysql.connector
import os
import random
import datetime

if __name__ == '__main__':
    config = {
        'host': os.environ['DB_NAME'],
        'user': os.environ['MYSQL_USER'],
        'password': os.environ['MYSQL_PASSWORD'],
        'database': os.environ['MYSQL_DATABASE'],
        'port' : int(os.environ['DB_PORT']),
    }
    db = mysql.connector.connect(**config)
    user_ids = [1] + [i for i in range(4,104)]
    
    for _ in range(10_000):

        user = random.random(user_ids)
        sql = 'INSERT INTO pofjes (user_id, price, date) VALUES (%s, %s, %s)'
        values = (f'{user}', '0.50', f'{datetime.now() - datetime.timedelta(seconds=int(random.random() * 5*365.25*24*3600))}')
        db.execute(sql, values)
        break
"