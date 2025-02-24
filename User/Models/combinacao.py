import os
import json

class Combinacao:
    def __init__(self, id: int, clima: str, id_itens_roupas: list, id_cliente: int):
        self.set_id(id)
        self.set_clima(clima)
        self.set_id_itens_roupas(id_itens_roupas)
        self.set_id_cliente(id_cliente)

    def __str__(self) -> str:
        return (f"Combinação:\n"
                f"id={self.__id}\n"
                f"clima={self.__clima}\n"
                f"id_itens={self.__id_itens_roupas}\n"
                f"id_cliente={self.__id_cliente}")

    def to_dict(self):
        return {
            'id': self.__id,
            'clima': self.__clima,
            'id_itens': self.__id_itens_roupas,
            'id_cliente': self.__id_cliente
        }

    def set_id(self, id):
        if isinstance(id, int):
            self.__id = id
        else:
            raise ValueError("ID inválido")

    def set_clima(self, clima):
        if isinstance(clima, str):
            self.__clima = clima
        else:
            raise ValueError("Clima inválido")

    def set_id_itens_roupas(self, id_itens_roupas):
        if isinstance(id_itens_roupas, list):
            self.__id_itens_roupas = id_itens_roupas
        else:
            raise ValueError("IDs de roupas inválidos")

    def set_id_cliente(self, id_cliente):
        if isinstance(id_cliente, int):
            self.__id_cliente = id_cliente
        else:
            raise ValueError("ID do cliente inválido")

    @property
    def id(self):
        return self.__id

    @property
    def clima(self):
        return self.__clima

    @property
    def id_itens_roupas(self):
        return self.__id_itens_roupas

    @property
    def id_cliente(self):
        return self.__id_cliente


class Combinacoes:
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for x in cls.objetos:
            if x.id > id:
                id = x.id

        obj.set_id(id + 1)
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for x in cls.objetos:
            if x.id == id:
                return x
        return None

    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x is not None:
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x is not None:
            cls.objetos.remove(x)
            cls.salvar()

    @classmethod
    def salvar(cls):
        if not os.path.exists('Data'):
            os.makedirs('Data')

        with open("Data/combinacao.json", mode="w") as arquivo:
            dados = [combinacao.to_dict() for combinacao in cls.objetos]
            json.dump(dados, arquivo, indent=4)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Data/combinacao.json", mode='r') as arquivo:
                combinacao_json = json.load(arquivo)
                for obj in combinacao_json:
                    combinacao = Combinacao(obj["id"], obj["clima"], obj["id_itens"], obj["id_cliente"])
                    cls.objetos.append(combinacao)
        except FileNotFoundError:
            pass