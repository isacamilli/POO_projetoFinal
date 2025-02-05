import json

class Cliente:
  def __init__(self, id : int, nome, email, senha, adm : bool = False):
    self.set_id(id)
    self.set_nome(nome)
    self.set_email(email) 
    self.set_senha(senha)
    self.set_adm(adm)
  
  def __str__(self):
    return f"{self.id} - {self.nome} - {self.email} - {self.fone}"
  
  def set_id(self, id):
    if isinstance(id, int): self.__id = id
    else: raise ValueError("id invalido")

  def set_nome(self, nome):
    if nome != None: self.__nome = nome     #if nome
    else: raise ValueError("nome invalido")

  def set_email(self, email):
    if not isinstance(email, str): raise ValueError("Email Invalido")

    self.__email = email 

  def set_senha(self, senha):
    if len(senha) >= 6: self.__senha = senha
    else: raise ValueError("Senha muito curta")

  def set_adm(self, adm):
    if isinstance(adm, bool): self.__adm = adm
    else: raise ValueError("adm invalido")

  
  @property 
  def id(self):
    return self.__id
  
  '''pra acessar é "Cliente.id" , como se fosse um atributo | sem isso mudaria o nome de id para get_id, e acessaria com "cliente.get_id()"'''

  @property
  def nome(self):
    return self.__nome
  
  @property
  def email(self):
    return self.__email 
  
  @property
  def senha(self):
    return self.__senha
  
  @property
  def adm(self):
    return self.__adm


class Clientes(Modelo_JSON): #seguir a ideia de asaph
