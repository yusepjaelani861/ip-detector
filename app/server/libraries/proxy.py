import requests
import pymysql.cursors
from ..config.mysql import host, user, password, database

def check_proxy(ip):
    try:
        db = check_from_db(ip)
        if db:
            return {
                "status": "success",
                "ip": db["ip"],
                "proxy": db["proxy"],
                "type": db["type"],
            }
        else:
            url = 'http://proxycheck.io/v2/' + ip + '?key=98b402-96855c-4500b8-c062s5&risk=1&vpn=1'
            data = requests.get(url).json()
            
            insert_to_db(ip, data[ip]["proxy"], data[ip]["type"])
            
            return {
                "status": "success",
                "ip": ip,
                "proxy": data[ip]["proxy"],
                "type": data[ip]["type"],
            }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }


def check_from_db(ip):
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.DictCursor,
        )
        
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM proxies WHERE ip = %s"
                cursor.execute(sql, (ip,))
                result = cursor.fetchone()
                return result
    except:
        return None
    
def insert_to_db(ip, proxy, type):
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.DictCursor,
        )
        
        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO proxies (ip, proxy, type) VALUES (%s, %s, %s)"
                cursor.execute(sql, (ip, proxy, type))
                connection.commit()
    except:
        return None