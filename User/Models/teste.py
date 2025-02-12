from cliente import Cliente,Clientes
from roupa import Roupa,Roupas
from tipo_roupa import Tipo_roupa,Tipos_roupas

id = 6665
nome = 'isaa'
email = 'isea'
fone= 57585
senha = 1244
adm = False

cliente_prova = Cliente(id,nome,email,fone,senha,adm)

roupa_prova = Roupa(1,"bella camicia",'branca',2,'strisce nere',2)

tipo_roupa_prova = Tipo_roupa(1,"blusa","dohsopfsh")

Clientes.inserir(cliente_prova)
Roupas.inserir(roupa_prova)
Tipos_roupas.inserir(tipo_roupa_prova)