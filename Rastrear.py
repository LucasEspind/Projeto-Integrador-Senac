class Rastrear:
    def __init__(self, IdItem):
        self._idItem = IdItem
        self._statusEntrega = "Pedido Realizado"
    
    @property
    def idItem(self):
        return self._idItem
    
    @idItem.setter
    def idItem(self, id):
        self._idItem = id

    @property
    def statusEntrega(self):
        return self._statusEntrega
    
    @statusEntrega.setter
    def statusEntrega(self, status):
        self._statusEntrega = status