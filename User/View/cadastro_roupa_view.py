import streamlit as st
from ..Models.roupa import Roupa, Roupas
from ..Models.tipo_roupa import Tipo_roupa, Tipos_roupas

class CadastroRoupaView:
    @staticmethod
    def tipo_existe(tipo_nome: str) -> bool:
        tipos = Tipos_roupas.listar()
        return any(t.nome == tipo_nome for t in tipos)

    @staticmethod
    def tipos() -> list[str]:
        tipos = Tipos_roupas.listar()
        return [t.nome for t in tipos]

    @staticmethod
    def cadastrar_roupa(nome_roupa, cor, tipo_nome: str, descricao_tipo: str, detalhes, id_cliente: int):
        if nome_roupa and cor and tipo_nome and detalhes:
            # Listar os tipos existentes e procurar o tipo digitado
            tipos = Tipos_roupas.listar()
            tipo_existente = next((tipo for tipo in tipos if tipo.nome == tipo_nome), None)

            if tipo_existente:
                tipo_id = tipo_existente.id
            else:
                # Se o tipo não existir, certifique-se de que a descrição foi preenchida
                if not descricao_tipo:
                    st.error("Por favor, preencha a descrição para o novo tipo")
                    return
                
                novo_id = len(tipos) + 1
                novo_tipo = Tipo_roupa(novo_id, tipo_nome, descricao_tipo)
                Tipos_roupas.inserir(novo_tipo)
                tipo_id = novo_id

            nova_roupa = Roupa(0, nome_roupa, cor, tipo_id, detalhes, id_cliente)
            Roupas.inserir(nova_roupa)
            st.success("Roupa cadastrada com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos para cadastrar a roupa")