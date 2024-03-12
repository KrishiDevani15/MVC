from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] ="ThePerfectorXD"
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='authentication'

mysql = MySQL(app)

if __name__ == '__main__':
    app.run(debug=True)

from controllers.auth_controller import *
from models.user import *
