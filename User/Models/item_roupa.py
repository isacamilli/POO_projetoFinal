import json
import os
from .roupa import Roupas

class Item_roupa:
    def __init__(self,id:int,lista_id_roupas:list):
        self.set_id(id)
        self.set_lista(lista_id_roupas)

    def __str__(self):
        return f"""Item_roupa:
                id={self.__id}
                , lista_id_roupas={self.__lista_id_roupas}"""

    def to_dict(self):
        return {
            'id': self.__id,
            'lista_id_roupas': self.__lista_id_roupas,
            }

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
    def inserir(cls,obj):
        cls.abrir()
        id = 0
        for x in cls.objetos:
            if x.id > id: id = x.id

        obj.set_id(id+1)

        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def listar_id(cls,id):
        cls.abrir()
        for x in cls.objetos:
            if x.id == id : return x
        return None
    
    
    @classmethod
    def listar_roupas(cls,id):
        roupas_lista = []

        cls.abrir()
        
        for x in cls.objetos:
            if x.id == id:
                for i in range(len(x.lista_id_roupas)):
                    num = x.lista_id_roupas[i]
                    print(num)
                    roupa = Roupas.listar_id(num)  # Aqui você deve garantir que `listar_id` retorna um objeto completo
                    if roupa:
                        print(roupa)  # Se a roupa for encontrada, adicione à lista
                        roupas_lista.append(roupa)
                        print(roupas_lista)
                return roupas_lista

        return None
        
    @classmethod
    def atualizar(cls,obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls,obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.salvar()

    @classmethod
    def salvar(cls):
        if not os.path.exists('Data'):
            os.makedirs('Data')

        with open("Data/item_roupa.json", mode="w") as arquivo:
            dados = [Item_roupa.to_dict() for Item_roupa in cls.objetos]
            print(dados)
            json.dump(dados, arquivo)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Data/item_roupa.json", mode='r') as arquivo:
                item_roupa_json = json.load(arquivo)
                for obj in item_roupa_json:
                    item_roupa = Item_roupa(obj["id"], obj["lista_id_roupas"])
                    cls.objetos.append(item_roupa)

        except FileNotFoundError:
            pass