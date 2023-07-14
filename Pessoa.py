from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, Nome, Cargo, Setor, Email, Password):
        self._nome = Nome
        self._cargo = Cargo
        self._setor = Setor
        self._email = Email
        self._password = Password

    @abstractmethod
    def get_permissao(self):
        pass

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, NovoNome):
        self._nome = NovoNome
    
    @property
    def cargo(self):
        return self._cargo
    
    @cargo.setter
    def cargo(self, NovoCargo):
        self._cargo = NovoCargo
    
    @property
    def setor(self):
        return self._setor
    
    @setor.setter
    def setor(self, NovoSetor):
        self._setor = NovoSetor

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, NovoEmail):
        self._email = NovoEmail

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, NovoPassword):
        self._Password = NovoPassword