from cliente import Cliente,Clientes
from roupa import Roupa,Roupas
from tipo_roupa import Tipo_roupa,Tipos_roupas
from item_roupa import Item_roupa,Itens_roupas

# cliente1 = Cliente(2,"isa",'email',1234,'senha',False)
# Clientes.inserir(cliente1)

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

itens_roupas1 = Item_roupa(4,[1,2])
Itens_roupas.inserir(itens_roupas1)
Itens_roupas.listar_roupas(1)