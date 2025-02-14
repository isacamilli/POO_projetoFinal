import os
import json

class Local:
  def __init__(self, id: int, cidade: str):
    self.set_id(id)
    self.set_cidade(cidade)

  def __str__(self):
    return f"Local:\n  id={self.__id}\n  cidade={self.__cidade}"
  
  def to_dict(self):
    return {
      'id': self.__id,
      'cidade': self.__cidade
    }

  def set_id(self, id):
    if isinstance(id, int):
      self.__id = id
    else:
      raise ValueError("ID do local inválido")

  def set_cidade(self, cidade):
    if isinstance(cidade, str):
      self.__cidade = cidade
    else:
      raise ValueError("Cidade inválida")

  @property
  def id(self):
    return self.__id

  @property
  def cidade(self):
    return self.__cidade
  

class Locais:
  objetos = []
  filename = "Data/local.json"

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = max([x.id for x in cls.objetos], default=0) + 1
    obj.set_id(id)    
    cls.objetos.append(obj)
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.objetos
  
  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    return next((x for x in cls.objetos if x.id == id), None)
  
  @classmethod
  def atualizar(cls, obj):
    x = cls.listar_id(obj.id)
    if x:
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
    directory = os.path.dirname(cls.filename)
    if not os.path.exists(directory):
      os.makedirs(directory)

    with open(cls.filename, 'w', encoding='utf-8') as f:
      json.dump([obj.to_dict() for obj in cls.objetos], f, ensure_ascii=False, indent=4)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    if os.path.exists(cls.filename) and os.path.getsize(cls.filename) > 0:
      try:
        with open(cls.filename, 'r', encoding='utf-8') as arquivo:
          locais_json = json.load(arquivo)
          for obj in locais_json:
            c = Local(obj["id"], obj["cidade"])
            cls.objetos.append(c)
      except json.JSONDecodeError:
        pass
