import streamlit as st
from ..View.login_view import Login_View
from .clima_ui import Mostrar_clima
from .roupa_ui import Mostrar_roupas
from .cadastro_roupa_ui import CadastroRoupa
from .adm_ui import AdmUI

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

        cls.__criar_admin_padrao()

        match st.session_state.page:
            case "home":
                cls.__cliente()
                
            case "login":
                cls.__login()
                
            case "admin":
                AdmUI.run()

    @classmethod
    def __criar_admin_padrao(cls):
        admin_existe = Login_View.verificar_admin_existente("admin", "admin")
        
        if not admin_existe:
            Login_View.criar_adm("admin", "admin", "1234", "1234", True)

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
        Mostrar_roupas.run()

    @classmethod
    def __cadastro_roupa(cls):
        st.markdown("<h1 style='text-align: center;'>🌤️ Cloud Wear</h1>", unsafe_allow_html=True)
        st.header("Cadastrar Nova Roupa")
        CadastroRoupa.run()