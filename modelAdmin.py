from modelPessoa import *


class Admin(Pessoa):
    def __init__(self, Nome, Cargo, Setor, Email, Login, Password):
        super().__init__(Nome, Cargo, Setor, Email, Password)
        self._permissao = "Admin"
        self._login = Login
    
    def get_permissao(self):
        return self._permissao

    @property
    def login(self):
        return self._login
    
    @login.setter
    def login(self, NovoLogin):
        self._login = NovoLogin