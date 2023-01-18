from dotenv import load_dotenv
from os import environ
from mysql.connector import connect,cursor
from mysql.connector.errors import InternalError,ProgrammingError
from logging import basicConfig,FileHandler,StreamHandler, DEBUG,INFO,ERROR,debug,info,error

# keys
load_dotenv('.env')

host = environ.get('host')
user = environ.get('user')
password = environ.get('password')
database = environ.get('database')

#Database
connect(host=host,user=user,password=password,database=database)
finnance_db =connect(host=host,user=user,password=password,database=database)
finnance = finnance_db.cursor(buffered=True)
finnance.execute('show tables')


#Log

Azul = '\033[94m'
Fim = '\033[0m'

filelog = FileHandler("logging.log","w",delay=True)
filelog.setLevel(ERROR)

basicConfig(
    level=DEBUG,
    encoding="UTF-8",
    datefmt= 'Data: %d/%m/%Y  Horário: %I:%M:%S %p',
    format=f"{Azul} %(levelname)s {Fim} | %(message)s - %(asctime)s",
    handlers=[filelog,StreamHandler()]
)
