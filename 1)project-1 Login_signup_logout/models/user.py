from app import mysql

def create_user(username,email,password):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO USER (username, email, password) VALUES(%s,%s,%s)",((username, email, password)))
    mysql.connection.commit()
    cur.close()

def get_user_by_username(email):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user WHERE email = %s", (email,))
    user = cur.fetchone()
    cur.close()
    return user
    