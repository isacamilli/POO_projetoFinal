import json
import os

class Tipo_roupa:
    def __init__(self,id,nome,descricao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)

    def __str__(self):
        return f"""Tipo_roupa:
        id={self.__id}
        , nome={self.__nome}
        , descricao={self.__descricao}"""
    
    def to_dict(self):
        return {
            'id': self.__id,
            'nome': self.__nome,
            'descricao': self.__descricao
            }
    
    def set_id(self,id):
        if isinstance(id,int): self.__id = id
        else: raise ValueError("ID tipo_roupa inválido")

    def set_nome(self,nome):
        if nome != None: self.__nome = nome
        else: raise ValueError("Nome tipo_roupa inválido")

    def set_descricao(self,descricao):
        if descricao != None: self.__descricao = descricao
        else: raise ValueError("Descrição inválida")

    @property
    def id(self):
        return self.__id
    
    @property 
    def nome(self):
        return self.__nome
    
    @property
    def descricao(self):
        return self.__descricao

class Tipos_roupas:
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
            if x.id == id:return x        
        return None
    
    @classmethod
    def atualizar(cls,obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x:
            cls.objetos.remove(x)
            cls.salvar()

    @classmethod
    def salvar(cls):
        if not cls.objetos:
            print("Nenhum tipo de roupa para salvar.")
            return

        if not os.path.exists("Data"):
            os.makedirs("Data")
        
        with open("Data/tipo_roupa.json", mode="w") as arquivo:
            dados = [tipo.to_dict() for tipo in cls.objetos]
            json.dump(dados, arquivo)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Data/tipo_roupa.json", mode="r") as arquivo:
                tipo_json = json.load(arquivo)
                for obj in tipo_json:
                    t_r = Tipo_roupa(obj["id"], obj["nome"], obj["descricao"])
                    cls.objetos.append(t_r)
        except FileNotFoundError:
            pass
