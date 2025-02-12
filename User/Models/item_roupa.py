class Item_roupa:
    def __init__(self,id:int,lista_id_roupas:list):
        self.set_id(id)
        self.set_lista(lista_id_roupas)

    def set_id(self,id):
        if isinstance(id,int): self.__id = id
        else: raise ValueError("ID item roupas inválido")

    def set_lista(self,lista_id):
        if len(lista_id) > 0 : self.__lista_id_roupas = lista_id
        else: raise ValueError("Lista itens roupas não pode estar vazia")

    @property
    def id(self):
        return self.__id
    
    @property
    def lista_id_roupas(self):
        return self.__lista_id_roupas
    

class Itens_roupas:
    objetos = []

    @classmethod
    def inserir(cls,)