import os
import json

class Local:
  def __init__(self,id:int, cidade : str):
    self.set_id(id)
    self.set_cidade(cidade)

  def __str__(self):
    return f"""Local:
    id={self.__id}
    , cidade={self.__cidade}"""
  
  def to_dict(self):
    return {
        'id': self.__id,
        'cidade': self.__cidade,
        }

  def set_id(self,id):
    if isinstance(id,int): self.__id = id
    else: raise ValueError("id local invalido")

  def set_cidade(self,cidade):
    if isinstance(cidade, str): self.__cidade = cidade
    else: raise ValueError("Cidade inváida")

  @property
  def id(self):
    return self.__id

  @property
  def cidade(self):
    return self.__cidade
  

class Locais:
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

  @staticmethod
  def salvar(usuario_id, cidade_nome, filename="Data/local.json"):
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
      os.makedirs(directory)

    if os.path.exists(filename) and os.path.getsize(filename) > 0:
      with open(filename, 'r', encoding='utf-8') as f:
        local_dict = json.load(f)
  
        if not isinstance(local_dict, dict):
          local_dict = {}
    else:
      local_dict = {}

    if usuario_id not in local_dict:
      local_dict[usuario_id] = []

    local_dict[usuario_id].append(cidade_nome)

    with open(filename, 'w', encoding='utf-8') as f:
      json.dump(local_dict, f, ensure_ascii=False, indent=4)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("Data/local.json", mode="r") as arquivo:
        locais_json = json.load(arquivo)
        for obj in locais_json:
          c = Local(obj["id"], obj["cidade"])
          cls.objetos.append(c)    

    except FileNotFoundError: pass