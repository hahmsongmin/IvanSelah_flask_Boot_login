import pymysql

MYSQL_HOST = 'localhost'
MYSQL_CONNECT = pymysql.connect(
    host=MYSQL_HOST,
    port=3306,
    user='root',
    passwd='gkaquf1@',
    db='login_db1',
    charset='utf8'
)

def conn_mysqldb():
    if not MYSQL_CONNECT.open:
        MYSQL_CONNECT.ping(reconnect=True)
    return MYSQL_CONNECT