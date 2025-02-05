class Cliente:
    def __init__(self) -> None:
        pass


class Roupa:
    def __init__(self,id:int, nome_roupa, cor,tipo,detalhes,id_cliente):
        self.set_id(id)

    def set_id(self,id):
        if isinstance(id,int): self.__id = id
        else: raise ValueError("ID inválido")

    def set_nomeRoupa(self,nome_roupa):
        if nome_roupa != None : self.__nome_roupa = nome_roupa
        else: raise ValueError("Nome inválido")

    def set_cor(self,cor):
        if cor != None : self.__cor = cor
        else: raise ValueError("Cor inválida")

    def set_tipo(self,tipo_roupa):
        if tipo_roupa != None : self.__tipo = tipo_roupa
        else: raise ValueError("")