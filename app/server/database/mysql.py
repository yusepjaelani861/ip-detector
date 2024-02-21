import pymysql.cursors
from ..config.mysql import host, user, password, database 

connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database,
    cursorclass=pymysql.cursors.DictCursor
)

def connect():
    return connection

with connection:
    with connection.cursor() as cursor:
        sql = "CREATE TABLE IF NOT EXISTS proxies (id INT AUTO_INCREMENT PRIMARY KEY, ip VARCHAR(50), proxy VARCHAR(255), type VARCHAR(255), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)"
        cursor.execute(sql)
        
        connection.commit()