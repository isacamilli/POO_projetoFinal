class Roupa:
    def __init__(self,id:int, nome_roupa, cor,tipo,detalhes,id_cliente:int):
        self.set_id(id)
        self.set_nomeRoupa(nome_roupa)
        self.set_cor(cor)
        self.set_tipo(tipo)
        self.set_detalhes(detalhes)
        self.set_idCliente(id_cliente)

    def __str__(self) -> str:
        return f"{self.__id} - {self.__nome_roupa} - {self.__cor} - {self.__tipo} - {self.__detalhes} - {self.__id_cliente}"


    def set_id(self,id):
        if isinstance(id,int): self.__id = id
        else: raise ValueError("ID inválido")

    def set_nomeRoupa(self,nome_roupa):
        if nome_roupa != None : self.__nome_roupa = nome_roupa
        else: raise ValueError("Nome inválido")

    def set_cor(self,cor):
        if cor != None : self.__cor = cor
        else: raise ValueError("Cor inválida")

    def set_tipo(self,tipo_roupa):
        if tipo_roupa != None : self.__tipo = tipo_roupa
        else: raise ValueError("Tipo inválido")

    def set_detalhes(self,detalhes):
        if detalhes != None: self.__detalhes = detalhes
        else: raise ValueError("Formato dos detalhes inválido")

    def set_idCliente(self,id_cliente):
        if isinstance(id_cliente,int): self.__id_cliente = id_cliente
        else: raise ValueError("id cliente na área roupa inválido")

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
    def tipo(self):
        return self.__tipo
    
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
    def excluir(cls,obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.salvar()