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
            salario float not null, 
            level int
            )'''
            )
        debug('table gastos')
        finnance.execute(
            '''create table if not exists Gastos
            (
            ID_gasto int primary key auto_increment,
            desc_gasto varchar(100) not null,
            valor_gasto float not null,
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
            valor_lucro float not null,
            FID_user int not null
            )
            '''
        )
        debug('verify user admin')
        finnance.execute('select * from usuarios where usuarios.username = "admin"')
        if len(finnance.fetchall()) > 0:
            info('user admin already exists')
        else:
            debug('create user admin')
            finnance.execute(
                '''insert into usuarios(
                    username,password,full_name,salario,level
                ) values(
                    'admin',
                    '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918',
                    'usuario administrador',
                    0,
                    99  
                )
                '''
        )
        finnance_db.commit()
    except InternalError as erro:
        error(erro)
    except ProgrammingError as erro:
        error(erro)


if __name__ == '__main__':
    check_table()