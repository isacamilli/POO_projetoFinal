import streamlit as st
from User.View.roupa_view import RoupaView  # Aqui estamos importando apenas a View

class UI_Roupas:

    @staticmethod
    def exibir_armario(id_cliente):
        st.title(f"Armário do Cliente {id_cliente}")
        RoupaView.armario(id_cliente)  # Usando a View para exibir o armário

    @staticmethod
    def cadastrar_roupa():
        st.title("Cadastrar Nova Roupa")

        # Formulário para cadastro de roupa
        with st.form(key='cadastro_roupa'):
            nome_roupa = st.text_input("Nome da Roupa")
            cor = st.text_input("Cor da Roupa")
            tipo = st.selectbox("Tipo de Roupa", [tipo.nome for tipo in Tipos_roupas.listar()])
            detalhes = st.text_area("Detalhes da Roupa")
            id_cliente = st.number_input("ID do Cliente", min_value=1)
            id_roupa = st.number_input("ID da Roupa (para associar com a roupa existente)", min_value=1)

            submit_button = st.form_submit_button(label="Cadastrar Roupa")

            if submit_button:
                RoupaView.cadastrar_roupa(nome_roupa, cor, tipo_roupa_obj.id, detalhes, id_roupa, id_cliente)
            else:
                st.error("Tipo de roupa não encontrado!")

    @staticmethod
    def rodar():
        menu = ["Exibir Armário", "Cadastrar Roupa"]
        opcao = st.sidebar.selectbox("Escolha a opção", menu)

        if opcao == "Exibir Armário":
            id_cliente = st.number_input("Digite seu ID de Cliente", min_value=1)
            UI_Roupas.exibir_armario(id_cliente)
        elif opcao == "Cadastrar Roupa":
            UI_Roupas.cadastrar_roupa()
