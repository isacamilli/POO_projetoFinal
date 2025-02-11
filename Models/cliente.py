import json
import re
import os

class Cliente:
  def __init__(self, id : int, nome, email, fone,senha, adm : bool = False):
    self.set_id(id)
    self.set_nome(nome)
    self.set_email(email)
    self.set_fone(fone)
    self.set_senha(senha)
    self.set_adm(adm)

  def __str__(self):
    return f"{self.id} - {self.nome} - {self.email} - {self.fone}"
  
  def set_id(self, id):
    if isinstance(id, int):
      self.__id = id
    else:
      raise ValueError('id invalido')
    
  def set_nome(self, nome):
    if nome:
      self.__nome = nome
    else:
      raise ValueError("nome nao pode ser invalido")
    
  def set_email(self, email):
    if not isinstance(email, str):
      raise ValueError("Email inválido")
    
    self.__email = email
    
  def set_fone(self, fone):
    if fone:
      self.__fone = fone
    else:
      raise ValueError("fone nao pode ser invalido")
    
  def set_senha(self, senha):
    self.__senha = senha

  def set_adm(self, adm):
    if isinstance(adm,bool):
      self.__adm = adm
    else:
      raise ValueError("adm invalido")
  
  @property
  def id(self):
    return self.__id
  
  @property
  def nome(self):
    return self.__nome
  
  @property
  def email(self):
    return self.__email
  
  @property
  def fone(self):
    return self.fone
  
  @property
  def senha(self):
    return self.__senha
  
  @property
  def adm(self):
    return self.__adm
    

class Clientes:
  objetos = [] 
  
  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = 0
    for x in cls.objetos:
      if x.id > id: id = x.id

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
      if x.id == id: return x
    return None
  
  @classmethod
  def atualizar(cls, obj):
    x = cls.listar_id(obj.id)
    if x != None:
      cls.objetos.remove(x)
      cls.objetos.append(obj)
      cls.salvar()        

  @classmethod
  def excluir(cls, obj):
    x = cls.listar_id(obj.id)
    if x != None:
      cls.objetos.remove(x)
      cls.salvar()        

  @classmethod
  def salvar(cls):
    if not os.path.exists('data'):
        os.makedirs('data')
    # open - cria e abre o arquivo clientes.json
    # vars - converte um objeto em um dicionário
    # dump - pega a lista de objetos e salva no arquivo
    with open("data/cliente.json", mode="w") as arquivo:
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("data/cliente.json", mode="r") as arquivo:
        clientes_json = json.load(arquivo)
        for obj in clientes_json:
          c = Cliente(obj["_Cliente__id"], obj["_Cliente__nome"], obj["_Cliente__email"], obj["_Cliente__fone"], obj["_Cliente__senha"], obj["_Cliente__adm"])
          cls.objetos.append(c)    

    except FileNotFoundError:
     # raise ValueError("Arquivo clientes não encontrado")
     pass