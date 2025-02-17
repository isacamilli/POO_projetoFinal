import streamlit as st
from User.View.login_view import Login_View
from Template.clima_ui import Mostrar_clima

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
        section = st.sidebar.selectbox("Menu", ["Home"])

        if section == "Home":
            st.markdown("<h1 style='text-align: center;'>🌤️ Cloud Wear</h1>", unsafe_allow_html=True)
            st.header("Confira o clima para escolher a combinação certa")
            Mostrar_clima.run()

        if st.sidebar.button("❌ Sair"):
            st.session_state.page = 'login'
            st.rerun()
