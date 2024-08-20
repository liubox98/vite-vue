import pymysql


def db_conn():
    return pymysql.connect(
        host="rm-uf6qww2lz4rznd3mido.mysql.rds.aliyuncs.com",
        port=3306,
        database="sga",
        charset="utf8mb4",
        user="dev_usr_focus",
        password="Dev_usr@focus",
        cursorclass=pymysql.cursors.DictCursor,
    )
