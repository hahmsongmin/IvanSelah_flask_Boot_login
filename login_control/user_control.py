from flask_login import UserMixin
from db_model.mysql import conn_mysqldb

class User(UserMixin):

    def __init__(self, user_id, user_email, user_password):
        self.id = user_id
        self.user_email = user_email
        self.user_password = user_password

    def get_id(self):
        return str(self.id)
    
    @staticmethod
    def get(user_id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = f"""select * from login_info where user_id = {user_id}"""
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            return None

        user = User(user_id=user[0], user_email=user[1], user_password=user[2])
        return user

    @staticmethod
    def find(user_email, user_password):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = f"""select * from login_info where user_email = '{user_email}' and user_password = '{user_password}'"""
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            return None

        user = User(user_id=user[0], user_email=user[1], user_password=user[2])
        return user

    @staticmethod
    def create(user_email, user_password):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = f"""insert into login_info(user_email, user_password)values('{user_email}','{user_password}')"""
        db_cursor.execute(sql)
        mysql_db.commit()
        return User.find(user_email, user_password)

    @staticmethod
    def delete(user_id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = f"""delete from login_info where user_id = {user_id}"""
        deleted = db_cursor.execute(sql)
        mysql_db.commit()
        return deleted