import mysql.connector
from mysql.connector import Error


def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="rm-uf6qww21z4rznd3mido.mysql.rds.aliyuncs.com",
            user="dev_user_focus",
            password="Dev_usr_focus",
            database="sga",
        )

        if connection.is_connected():
            print("成功连接到 MySQL 数据库")
            db_info = connection.get_server_info()
            print("MySQL 服务器版本:", db_info)

            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            db_name = cursor.fetchone()
            print("当前连接的数据库:", db_name)

    except Error as e:
        print("连接 MySQL 数据库失败:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL 连接已关闭")


if __name__ == "__main__":
    connect_to_mysql()
