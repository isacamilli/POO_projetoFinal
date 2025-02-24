import streamlit as st
from ..View.cadastro_roupa_view import CadastroRoupaView

def check_tipo():
    tipo_selecionado = st.session_state.tipo if "tipo" in st.session_state else ""
    if tipo_selecionado == "Novo Tipo":
        st.session_state.descricao_tipo = ""
    elif tipo_selecionado:
        if CadastroRoupaView.tipo_existe(tipo_selecionado):
            st.session_state.descricao_tipo = ""

class CadastroRoupa:
    @staticmethod
    def run():
        id_cliente = st.session_state.user.id

        tipos_roupa = CadastroRoupaView.tipos()
        tipos_roupa.append("Novo Tipo")  # Adiciona a opção para adicionar um novo tipo

        tipo = st.selectbox("Tipo", tipos_roupa, key="tipo", on_change=check_tipo)

        if tipo == "Novo Tipo":
            novo_tipo = st.text_input("Novo Tipo de Roupa", key="novo_tipo")
            descricao_tipo = st.text_input("Descrição do Novo Tipo", key="descricao_tipo")
        else:
            descricao_tipo = st.session_state.descricao_tipo if "descricao_tipo" in st.session_state else ""

        nome = st.text_input("Nome", key="nome")

        cor = st.text_input("Cor", key="cor")

        detalhes = st.text_input("Detalhes", key="detalhes")

        if st.button("Cadastrar"):
            # Recupera os valores com session state
            nome = st.session_state.nome
            cor = st.session_state.cor
            tipo = st.session_state.tipo if st.session_state.tipo != "Novo Tipo" else st.session_state.novo_tipo
            detalhes = st.session_state.detalhes
            descricao_tipo = st.session_state.descricao_tipo if "descricao_tipo" in st.session_state else ""

            if not nome or not cor or not tipo or not detalhes:
                st.error("Por favor, preencha todos os campos obrigatórios.")
            else:
                CadastroRoupaView.cadastrar_roupa(nome, cor, tipo, descricao_tipo, detalhes, id_cliente)