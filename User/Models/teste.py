from cliente import Cliente, Clientes
from roupa import Roupa, Roupas
from tipo_roupa import Tipo_roupa, Tipos_roupas
from item_roupa import Item_roupa, Itens_roupas
from clima import Periodo_Clima, Climas
from combinacao import Combinacao, Combinacoes
from local import Local, Locais

# Teste Cliente
cliente1 = Cliente(2, "Gust", "email", 1234, "senha", False)
Clientes.inserir(cliente1)

print("\nLista de Clientes:")
for cliente in Clientes.listar():
  print(cliente)

# Teste Roupa
roupas = [
  Roupa(1, "Mizuno", "Preta", 2, "Strisce bianche", 1),
  Roupa(5, "Maglietta", "Azzura", 1, "Tank top", 1),
  Roupa(90, "Scarpe", "Rosa", 3, "Nere", 2)
]

for roupa in roupas:
  Roupas.inserir(roupa)

print("\nLista de Roupas:")
for roupa in Roupas.listar():
  print(roupa)

# Teste Tipo de Roupa
tipos_roupa = [
  Tipo_roupa(3, "Pantaloni", "Larghi"),
  Tipo_roupa(2, "Maglietta", "Cotone")
]

for tipo in tipos_roupa:
  Tipos_roupas.inserir(tipo)

print("\nLista de Tipos de Roupa:")
for tipo in Tipos_roupas.listar():
  print(tipo)

# Teste Item Roupa
itens_roupas1 = Item_roupa(4, [1, 2])
Itens_roupas.inserir(itens_roupas1)

print("\nLista de Itens de Roupa para o ID 1:")
Itens_roupas.listar_roupas(1)

# Teste Clima
clima1 = Periodo_Clima(1, "Frio")
clima1.clima_cidade()
Climas.salvar_clima(clima1)

# Teste Combinação
combinacao1 = Combinacao(1, "Natal", 1)
Combinacoes.inserir(combinacao1)

print("\nLista de Combinações:")
for combinacao in Combinacoes.listar():
  print(combinacao)

# Teste Local
locais = [
  Local(1, "São Paulo"),
  Local(2, "Rio de Janeiro")
]

for local in locais:
  Locais.inserir(local)

print("\nLista de Locais:")
for local in Locais.listar():
  print(local)

# Testando busca por ID
print("\nBuscando Local com ID 1:")
print(Locais.listar_id(1))