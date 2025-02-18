from cliente import Cliente,Clientes
from roupa import Roupa,Roupas
from tipo_roupa import Tipo_roupa,Tipos_roupas
from item_roupa import Item_roupa,Itens_roupas
from clima import Periodo_Clima, climas
from combinacao import Combinacao, Combinacoes

# #teste cliente
# cliente1 = Cliente(2,"gust",'email',1234,'senha',False)
# Clientes.inserir(cliente1)

# x = Clientes.listar()
# for i in x:
#   print(i)

# roupa1 = Roupa(1,"mizuno",'preta',2,'strisce bianche',1)
# roupa2 = Roupa(5,"maglietta",'azzura',1,'tank top',1)
# roupa3 = Roupa(90,"scarpe",'rosa',3,'nere',2)

# Roupas.inserir(roupa1)
# Roupas.inserir(roupa2)
# Roupas.inserir(roupa3)

# tipo_roupa1 = Tipo_roupa(3,'pantaloni','larghi')
# tipo_roupa2 = Tipo_roupa(2,"maglietta","cotone")

# Tipos_roupas.inserir(tipo_roupa1)
# Tipos_roupas.inserir(tipo_roupa2)

# itens_roupas1 = Item_roupa(4,[1,2])
# Itens_roupas.inserir(itens_roupas1)
# Itens_roupas.listar_roupas(1)

# clima1 = Periodo_Clima(1,"natal")
# clima1.clima_cidade()
# climas.salvar_clima_em_json(clima1)

# combinacao1 = Combinacao(1,"natal",1)
# Combinacoes.inserir(combinacao1)

# cliente_oto = Cliente(1,"oi",'oi',136,'sd',False)
# Clientes.inserir(cliente_oto)


Clientes.excluir(Cliente(1,"gust",'email',1234,'senha',False))