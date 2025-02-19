import os
import json
import requests
from datetime import datetime

class Periodo_Clima:
  def __init__(self,id, cidade):
    self.set_id(id)
    self.set_cidade(cidade)

  def __str__(self) -> str:
    return f"""Periodo_clima:
              id={self.__id} 
              , cidade= {self.__cidade}"""

  def set_id(self,id):
     if isinstance(id,int): self.__id = id
     else: raise ValueError("id clima inválido")

  def set_cidade(self, cidade):
    if isinstance(cidade, str): self.__cidade = cidade
    else: raise ValueError("Cidade invalida")

  @property
  def id(self):
     return self.__id

  @property
  def cidade(self):
    return self.__cidade
  
  @property
  def clima(self):
    return self.__clima

  @property
  def data(self):
    return self.__data

  @property
  def pais(self):
    return self.__pais
  
  @property
  def temperatura(self):
    return self.__temperatura
  
  @property
  def periodo(self):
    return self.__periodo

  @property
  def sensacao_termica(self):
    return self.__sensacao_termica
  
  def clima_cidade(self):
    url = f"http://api.openweathermap.org/../../data/2.5/weather?q={self.cidade}&appid=c5c2e778103223f1d989ac03ad6fcaee&units=metric&lang=pt_br"
    resposta = requests.get(url)

    #print(f"Status code da API: {resposta.status_code}")
    
    if resposta.status_code == 200: # 200 é uma resposta positiva da api
      dados = resposta.json()
      self.__pais = dados['sys']['country']
      self.__clima = dados['weather'][0]['description']    # ['weather'][0]['main'] pega um clima mais geral, mas está em inglês
      self.__temperatura = dados['main']['temp']
      self.__sensacao_termica = dados['main']['feels_like']
      self.__data = datetime.now()
      self.__periodo = self.determinar_periodo()

    else:
      self.__clima = "indisponivel"
      self.__temperatura = "indisponivel"
      self.__sensacao_termica = "indisponivel"
      self.__data = "indisponivel"
      self.__periodo = "indisponivel"


  def determinar_periodo(self):
    mes = self.data.month
    if mes in [12, 1, 2]: return "Inverno"
    elif mes in [3, 4, 5]: return "Primavera"
    elif mes in [6, 7, 8]: return "Verão"
    elif mes in [9, 10, 11]: return "Outono"


  @clima.setter   #setter define o valor de um atributo privado
  def clima(self, value):
    self.__clima = value

  @data.setter
  def data(self, value):
    self.__data = value

  @periodo.setter
  def periodo(self, value):
    self.__periodo = value


class Climas:
  objetos = []

  @staticmethod
  def salvar_clima(Periodo_Clima, filename="Data/clima.json"):
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
      os.makedirs(directory)

    if os.path.exists(filename):
      with open(filename, 'r', encoding='utf-8') as f:
        clima_dict = json.load(f)
        if not isinstance(clima_dict, dict):
          clima_dict = {} 
    else:
      clima_dict = {}

    # Verifica se a cidade já existe
    if Periodo_Clima.cidade in clima_dict:
      # Se a cidade já existe, mantém o mesmo id e atualiza os dados
      clima_dict[Periodo_Clima.cidade]["clima"] = Periodo_Clima.clima
      clima_dict[Periodo_Clima.cidade]["pais"] = Periodo_Clima.pais
      clima_dict[Periodo_Clima.cidade]["data"] = Periodo_Clima.data.strftime('%d/%m/%Y %H:%M')
      clima_dict[Periodo_Clima.cidade]["temperatura"] = Periodo_Clima.temperatura
      clima_dict[Periodo_Clima.cidade]["sensacao_termica"] = Periodo_Clima.sensacao_termica
      clima_dict[Periodo_Clima.cidade]["periodo"] = Periodo_Clima.periodo
    else:
      # Caso a cidade não exista, cria um novo id e adiciona os dados
      last_id = max([clima['id'] for clima in clima_dict.values()], default=0)
      new_id = last_id + 1

      clima_data = {
          "id": new_id,
          "cidade": Periodo_Clima.cidade,
          "pais": Periodo_Clima.pais,
          "data": Periodo_Clima.data.strftime('%d/%m/%Y %H:%M'),
          "clima": Periodo_Clima.clima,
          "periodo": Periodo_Clima.periodo,
          "temperatura": Periodo_Clima.temperatura,
          "sensacao_termica": Periodo_Clima.sensacao_termica
      }

      clima_dict[Periodo_Clima.cidade] = clima_data

    # Salva os dados (seja alterados ou novos)
    with open(filename, 'w', encoding='utf-8') as f:
      json.dump(clima_dict, f, ensure_ascii=False, indent=4)