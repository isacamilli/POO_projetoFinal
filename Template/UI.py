import streamlit as st
from User.View.login_view import Login_View
from Template.clima_ui import Mostrar_clima
from Template.roupa_ui import UI_Roupas  # Importando a UI_Roupas da roupa_ui

class UI:
    @classmethod
    def Run(cls):
        if 'page' not in st.session_state:
            st.session_state.page = 'login'

        if 'user' not in st.session_state:
            st.session_state.user = None

        st.set_page_config(
            page_title="Cloud Wear",
            page_icon="🌤️",
            layout="wide",
            initial_sidebar_state="expanded"
        )

        if st.session_state.page == "home":
            cls.__cliente()
        elif st.session_state.page == "login":
            cls.__login()

    @classmethod
    def __login(cls):
        st.markdown("<h1 style='text-align: center;'>🌤️ Cloud Wear</h1>", unsafe_allow_html=True)
        
        with st.container():
            tabs = st.tabs(["🔑 Entrar", "📝 Cadastro"])
            
            with tabs[0]:
                st.subheader("Acesse sua conta")
                usuario = st.text_input("Nome de usuário ou Email", key="login_username")
                senha = st.text_input("Senha", type="password", key="login_password")
                if st.button("Entrar"):
                    Login_View.login_authentication(usuario, senha)

            with tabs[1]:
                st.subheader("Criar uma nova conta")
                usuario = st.text_input("Nome", key="register_username")
                email = st.text_input("Email", key="register_email")
                fone = st.text_input("Telefone", key="register_tel")
                senha = st.text_input("Senha", type="password", key="register_password")
                if st.button("Cadastrar"):
                    Login_View.register_authentication(usuario, email, fone, senha)

    @classmethod
    def __cliente(cls):
        section = st.sidebar.selectbox("Menu", ["Home", "Armário", "Cadastro de Roupa"])

        if section == "Home":
            cls.__home()
        elif section == "Armário":
            cls.__armario()
        elif section == "Cadastro de Roupa":
            cls.__cadastro_roupa()

        if st.sidebar.button("❌ Sair"):
            st.session_state.page = 'login'
            st.rerun()

    @classmethod
    def __home(cls):
        st.markdown("<h1 style='text-align: center;'>🌤️ Cloud Wear</h1>", unsafe_allow_html=True)
        st.header("Confira o clima para escolher a combinação certa")
        Mostrar_clima.run()

    @classmethod
    def __armario(cls):
        st.markdown("<h1 style='text-align: center;'>🌤️ Cloud Wear</h1>", unsafe_allow_html=True)
        st.header("Roupas no armário")

        # Usando a UI_Roupas da roupa_ui para exibir o armário
        UI_Roupas.exibir_armario(1)  # Exibe o armário de um cliente (id_cliente = 1)

    @classmethod
    def __cadastro_roupa(cls):
        st.markdown("<h1 style='text-align: center;'>🌤️ Cloud Wear</h1>", unsafe_allow_html=True)
        st.header("Cadastrar Nova Roupa")


        if st.button("Cadastrar"):
            # Usando a UI_Roupas para cadastrar a roupa
            UI_Roupas.cadastrar_roupa()  # Chama a função de cadastro diretamente da UI_Roupas
            st.success("Roupa cadastrada com sucesso!")
