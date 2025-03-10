import json
import os

class Roupa:
    def __init__(self,id:int, nome_roupa, cor,tipo:int,detalhes,id_cliente:int):
        self.set_id(id)
        self.set_nomeRoupa(nome_roupa)
        self.set_cor(cor)
        self.set_idTipo(tipo)
        self.set_detalhes(detalhes)
        self.set_idCliente(id_cliente)

    def __str__(self) -> str:
        return f"""Roupa:
                  id={self.__id} 
                 , nome_roupa= {self.__nome_roupa} 
                 , cor= {self.__cor} 
                 , id_tipo= {self.__id_tipo} 
                 , detalhes= {self.__detalhes} 
                 , id_cliente= {self.__id_cliente}"""

    def to_dict(self):
        return {
            'id': self.__id,
            'nome_roupa': self.__nome_roupa,
            'cor': self.__cor,
            'id_tipo': self.__id_tipo,
            'detalhes': self.__detalhes,
            'id_cliente': self.__id_cliente
            }


    def set_id(self,id):
        if isinstance(id,int): self.__id = id
        else: raise ValueError("ID inválido")

    def set_nomeRoupa(self,nome_roupa):
        if nome_roupa != None : self.__nome_roupa = nome_roupa
        else: raise ValueError("Nome inválido")

    def set_cor(self,cor):
        if cor != None : self.__cor = cor
        else: raise ValueError("Cor inválida")

    def set_idTipo(self,tipo_roupa):
        if isinstance(tipo_roupa,int) : self.__id_tipo = tipo_roupa
        else: raise ValueError("Tipo inválido")

    def set_detalhes(self,detalhes):
        if detalhes != None: self.__detalhes = detalhes
        else: raise ValueError("Formato dos detalhes inválido")

    def set_idCliente(self,id_cliente):
        if isinstance(id_cliente,int): self.__id_cliente = id_cliente
        else: raise ValueError("id Roupa na área roupa inválido")

    @property
    def id(self):
        return self.__id
    
    @property
    def nome_roupa(self):
        return self.__nome_roupa
    
    @property
    def cor(self):
        return self.__cor
    
    @property
    def id_tipo(self):
        return self.__id_tipo
    
    @property
    def detalhes(self):
        return self.__detalhes
    
    @property
    def id_cliente(self):
        return self.__id_cliente

class Roupas:
    objetos = []

    @classmethod
    def inserir(cls,obj):
        cls.abrir()
        id = 0
        for x in cls.objetos:
            if x.id > id : id = x.id

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
            if x.id == id: return x
        return None
    
    @classmethod
    def atualizar(cls,obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, id):
        cls.abrir()
        roupa = cls.listar_id(id)
        if roupa is not None:
            cls.objetos.remove(roupa)
            cls.salvar()
            return True
        return False

    @classmethod
    def salvar(cls):
        if not os.path.exists('Data'):
            os.makedirs('Data')

        with open("Data/roupa.json", mode="w") as arquivo:
            dados = [Roupa.to_dict() for Roupa in cls.objetos]
            print(dados)
            json.dump(dados, arquivo)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Data/roupa.json", mode='r') as arquivo:
                roupas_json = json.load(arquivo)
                for obj in roupas_json:
                    roupa = Roupa(obj["id"], obj["nome_roupa"],obj["cor"],obj["id_tipo"], obj["detalhes"],obj["id_cliente"])
                    cls.objetos.append(roupa)
        
        except FileNotFoundError:
           # raise ValueError("Arquivo roupas não encontrado")
            pass