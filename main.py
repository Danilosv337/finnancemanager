from dotenv import load_dotenv
from os import environ
from mysql.connector import connect,cursor

load_dotenv('.env')

host = environ.get('host')
user = environ.get('user')
password = environ.get('password')
database = environ.get('database')

connect(host=host,user=user,password=password,database=database)
finnance_db =connect(host=host,user=user,password=password,database=database)
finnance = finnance_db.cursor()
finnance.execute('show tables')
print(finnance.fetchall())