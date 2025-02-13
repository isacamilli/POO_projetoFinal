import os
import json

class Combinacao:
  def __init__(self, id: int, clima: str, id_itens_roupas: int):
    self.set_id(id)
    self.set_id_itens_roupas(id_itens_roupas)
    self.set_clima(clima)

  def __str__(self) -> str:
    return f"Combinação:
              id={self.__id} 
              , clima= {self.__clima}
              , id_itens= {self.__id_itens_roupas}"
  
  def to_dict(self):
    return {
        'id': self.__id,
        'clima': self.__clima,
        'id_itens': self.__id_itens_roupas,
        }

  def set_id(self, id):
    if isinstance(id, int):
      self.__id = id
    else:
      raise ValueError("id invalido")

  def set_id_itens_roupas(self, id_itens_roupas):
    if isinstance(id_itens_roupas, int):
      self.__id_itens_roupas = id_itens_roupas
    else:
      raise ValueError("id de roupa invalido")

  def set_clima(self, clima):
    if isinstance(clima, str):
      self.__clima = clima
    else:
      raise ValueError("clima invalido")

  @property
  def id(self):
    return self.__id

  @property
  def id_itens_roupas(self):
    return self.__id_itens_roupas

  @property
  def clima(self):
    return self.__clima

  def verificar_ids(self):
    print(f"ID: {self.id} - ID Itens Roupas: {self.id_itens_roupas}")


class Combinacoes:
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
      if not os.path.exists('Data'):
          os.makedirs('Data')

      with open('Data/combinacao.json', mode='w') as arquivo:
          json.dump(cls.objetos,arquivo,default=vars)

  @classmethod
  def abrir(cls):
      cls.objetos = []
      try:
          with open("Data/combinacao.json", mode='r') as arquivo:
              combinacao_json = json.load(arquivo)
              for obj in combinacao_json:
                  combinacao = Combinacao(obj["id"], obj["clima"], obj["id_itens"])
                  cls.objetos.append(combinacao)

      except FileNotFoundError:
          pass
