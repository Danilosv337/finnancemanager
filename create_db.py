from config import *

def check_table():
    try:
        debug("verify table usuarios exist")

        debug('table user´s')
        finnance.execute(
            '''create table if not exists usuarios 
            (
            ID_user int primary key auto_increment, 
            username varchar(60) not null, 
            password varchar(255) not null, 
            full_name varchar(150) not null, 
            email varchar(150), 
            salario int not null, 
            level int
            )'''
            )
        debug('table gastos')
        finnance.execute(
            '''create table if not exists Gastos
            (
            ID_gasto int primary key auto_increment,
            desc_gasto varchar(100) not null,
            valor_gasto int not null,
            FID_user int not null
            )
            '''
        )
        debug('table lucros')
        finnance.execute(
            '''create table if not exists Lucros
            (
            ID_lucro int primary key auto_increment,
            desc_lucro varchar(100) not null,
            valor_lucro int not null,
            FID_user int not null
            )
            '''
        )
        finnance_db.commit()
    except InternalError as erro:
        error(erro)
    except ProgrammingError as erro:
        error(erro)


