class Item:
    def __init__(self, Nome, Quantidade, Preco, VendasFeitas):
        self._nome = Nome
        self._quantidade = Quantidade
        self._preco = Preco
        self._vendasFeitas = VendasFeitas
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, NovoNome):
        self._nome = NovoNome
    
    @property
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, NovoQuantidade):
        self._quantidade = NovoQuantidade
    
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, NovoPreco):
        self._preco = NovoPreco
    
    @property
    def vendasFeitas(self):
        return self._vendasFeitas
    
    @vendasFeitas.setter
    def vendasFeitas(self, NovoVendasFeitas):
        self._vendasFeitas = NovoVendasFeitas