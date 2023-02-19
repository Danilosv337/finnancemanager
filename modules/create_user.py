from .config import *
from hashlib import sha256

username = input("Qual o username? ") 
password = input("Qual sua senha? ") 
full_name = input("Qual o nome completo? ") 
email = input("Qual o email? ") 
start_wage = input("Qual salário Inicial? ") 


password = password.encode()
password = sha256(password).hexdigest()

finnance.execute(f'INSERT INTO usuarios (username,password,full_name,email,salario) \
     VALUES ("{username}","{password}","{full_name}","{email}",{start_wage})')

finnance_db.commit()