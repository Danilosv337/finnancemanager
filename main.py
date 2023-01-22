from config import finnance
from hashlib import sha256

class Usuario:
    def __init__(self):
        self.ID_user = None
    def login(self,user,password):
        password = password.encode()
        password = sha256(password).hexdigest()
        finnance.execute(f'select * from usuarios where username like "{user}"')
        conta = finnance.fetchall()
        if len(conta) == 0:
            self.ID_user = None
        elif password == conta[0][2]:
            self.ID_user = conta[0][0]
            return self.ID_user
        else: 
            self.ID_user = None


