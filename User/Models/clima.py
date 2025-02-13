import os
import json
import requests
from datetime import datetime

class Periodo_Clima:
  def __init__(self, cidade):
    self.set_cidade(cidade)

  def __str__(self):
    return f"Cidade: {self.cidade}|{self.pais} - Data: {self.data.strftime('%d/%m/%Y %H:%M')} - Clima: {self.clima} - Período: {self.periodo} - Temperatura: {self.temperatura}°C - Sensação Térmica: {self.sensacao_termica}°C"
  

  def set_cidade(self, cidade):
    if isinstance(cidade, str): self.__cidade = cidade
    else: raise ValueError("Cidade invalida")

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
  def periodo(self):
    return self.__periodo

  def clima_cidade(self):
    url = f"http://api.openweathermap.org/../../data/2.5/weather?q={self.cidade}&appid=c5c2e778103223f1d989ac03ad6fcaee&units=metric&lang=pt_br"
    resposta = requests.get(url)

    #print(f"Status code da API: {resposta.status_code}")
    
    if resposta.status_code == 200: # 200 é uma resposta positiva da api
      dados = resposta.json()
      self.pais = dados['sys']['country']
      self.clima = dados['weather'][0]['description']    # ['weather'][0]['main'] pega um clima mais geral, mas está em inglês
      self.temperatura = dados['main']['temp']
      self.sensacao_termica = dados['main']['feels_like']
      self.data = datetime.now()
      self.periodo = self.determinar_periodo()

    else:
      self.clima = "indisponivel"
      self.temperatura = "indisponivel"
      self.sensacao_termica = "indisponivel"
      self.data = "indisponivel"
      self.periodo = "indisponivel"


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


class climas:
  objetos = []

  @staticmethod
  def salvar_clima_em_json(periodo_clima, filename="Data/clima.json"):
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

    clima_data = {
      "cidade": periodo_clima.cidade,
      "pais": periodo_clima.pais,
      "data": periodo_clima.data.strftime('%d/%m/%Y %H:%M'),
      "clima": periodo_clima.clima,
      "periodo": periodo_clima.periodo,
      "temperatura": periodo_clima.temperatura,
      "sensacao_termica": periodo_clima.sensacao_termica
    }

    clima_dict[periodo_clima.cidade] = clima_data

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(clima_dict, f, ensure_ascii=False, indent=4)
