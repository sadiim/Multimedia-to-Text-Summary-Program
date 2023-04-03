import sqlite3 as sql


def create_table():
    conn = sql.connect('table1.db')
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS USERS(
    id Integer PRIMARY KEY,
    username text,
    password text
    )""")
    conn.commit()
    conn.close()


def insert(username, password):
    conn = sql.connect('table1.db')
    cursor = conn.cursor()

    add_command = """INSERT INTO USERS (username, password) VALUES{}"""
    data = (username, password)

    cursor.execute(add_command.format(data))

    conn.commit()
    conn.close()


def print_all():
    conn = sql.connect('table1.db')
    cursor = conn.cursor()

    cursor.execute("""SELECT * from USERS""")
    list_all = cursor.fetchall()

    for user in list_all:
        print(user)

    conn.close()


def search_username(username):
    conn = sql.connect('table1.db')
    cursor = conn.cursor()

    search_command = """SELECT * from USERS WHERE username = '{}'"""
    cursor.execute(search_command.format(username))

    user = cursor.fetchone()

    conn.close()
    return user


def update__password(username, newPassword):
    conn = sql.connect('table1.db')
    cursor = conn.cursor()

    upd_command = """"UPDATE USERS SER password = '{}' WHERE username = '{}'"""
    cursor.execute(upd_command.format(newPassword, username))

    conn.commit()
    conn.close()


def delete_account(username):
    conn = sql.connect('table1.db')
    cursor = conn.cursor()

    dlt_command = """DELETE from USERS WHERE username = '{}'"""
    cursor.execute(dlt_command.format(username))

    conn.commit()
    conn.close()


def delete_table():
    conn = sql.connect('table1.db')
    cursor = conn.cursor()

    cursor.execute("""DROP TABLE USERS """)

    conn.commit()
    conn.close()