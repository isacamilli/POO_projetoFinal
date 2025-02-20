import streamlit as st
from collections import defaultdict
from User.View.login_view import Login_View
from User.View.roupa_view import RoupaView
from ..Template.clima_ui import Mostrar_clima
# from ..Template.adm_ui import AdmUI

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

        match st.session_state.page:
                
            case "home":
                cls.__cliente()
                
            case "login":
                cls.__login()

            # case "adm":
            #     AdmUI.adm()

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

        roupas = RoupaView.armario(1)  # Obtendo as roupas do usuário
        roupas_por_tipo = defaultdict(list)

        for roupa in roupas:
            roupas_por_tipo[roupa.tipo].append(roupa)

        for tipo, lista_roupas in roupas_por_tipo.items():
            st.subheader(f"🧥 {tipo}")
            for roupa in lista_roupas:
                with st.expander(roupa.nome):
                    st.text(f"Cor: {roupa.cor}")
                    st.text(f"Detalhes: {roupa.detalhes}")

    @classmethod
    def __cadastro_roupa(cls):
        st.markdown("<h1 style='text-align: center;'>🌤️ Cloud Wear</h1>", unsafe_allow_html=True)
        st.header("Cadastrar Nova Roupa")

        nome_roupa = st.text_input("Nome da Roupa")
        cor_roupa = st.text_input("Cor da Roupa")
        tipo_roupa = st.text_input("Tipo da Roupa")
        desc_roupa = st.text_input("Descrição da Roupa")

        if st.button("Cadastrar"):
            RoupaView.cadastrar_roupa(nome_roupa, cor_roupa, int(tipo_roupa), desc_roupa, 0, 1)
            st.success("Roupa cadastrada com sucesso!")
