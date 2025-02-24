from ..Models.roupa import Roupas
from ..Models.tipo_roupa import Tipos_roupas

class RoupaView:
    @staticmethod
    def armario(id_cliente):
        armario = []

        # Busca as roupas do cliente
        for roupa in Roupas.listar():
            if roupa.id_cliente == id_cliente:
                armario.append(roupa)

        if not armario:
            return "Nenhuma roupa cadastrada no armário"

        roupas_por_tipo = {}
        for roupa in armario:
            tipo_obj = Tipos_roupas.listar_id(roupa.id_tipo)
            nome_tipo = tipo_obj.nome
            if nome_tipo not in roupas_por_tipo:
                # Aqui, em vez de apenas criar uma lista, usa-se uma tupla com a descrição e a lista de roupas
                roupas_por_tipo[nome_tipo] = (tipo_obj.descricao, [])
            roupas_por_tipo[nome_tipo][1].append(roupa)

        return roupas_por_tipo
    
    @staticmethod
    def excluir_roupa(id_roupa):
        try:
            return Roupas.excluir(id_roupa)
        except Exception as e:
            print(f"Erro ao excluir roupa: {e}")
            return False