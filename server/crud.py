from db import db_conn


def fetch_all_data(table):
    connection = db_conn()
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM {table}"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        connection.close()
    return result


def insert_data(data, table):
    connection = db_conn()
    try:
        with connection.cursor() as cursor:
            sql = f"""
                INSERT INTO {table} (
                    role_number, type, name, aos, level,
                    g1, g1_s1, g1_s2, g2, g2_s1, g2_s2,
                    g3, g3_s1, g3_s2
                ) VALUES (%s, %s, %s, %s, %s,
                          %s, %s, %s, %s, %s, %s,
                          %s, %s, %s)
            """
            cursor.execute(
                sql,
                (
                    1506275,
                    data.type,
                    data.name,
                    data.aos,
                    data.level,
                    data.g1,
                    data.g1_s1,
                    data.g1_s2,
                    data.g2,
                    data.g2_s1,
                    data.g2_s2,
                    data.g3,
                    data.g3_s1,
                    data.g3_s2,
                ),
            )
            connection.commit()
    finally:
        connection.close()
