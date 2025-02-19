import streamlit as st
from User.View.roupa_view import RoupaView

class UI_Roupas:
    @staticmethod
    def exibir_armario(id_cliente):
        st.title(f"Armário do Cliente {id_cliente}")
        RoupaView.armario(id_cliente)

    @staticmethod
    def cadastrar_roupa():
        # roupa nova
        with st.form(key='cadastro_roupa'):
            nome_roupa = st.text_input("Nome da Roupa")
            cor = st.text_input("Cor da Roupa")
            tipo = st.text_area("Tipo de Roupa")
            detalhes = st.text_area("Detalhes da Roupa")

            submit_button = st.form_submit_button(label="Cadastrar Roupa")

            if submit_button:
                RoupaView.cadastrar_roupa(nome_roupa, cor, tipo, detalhes)
            else:
                st.error("Tipo de roupa não encontrado!")