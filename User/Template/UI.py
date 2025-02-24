import streamlit as st
from collections import defaultdict
from ..View.login_view import Login_View
from ..Template.clima_ui import Mostrar_clima
from .roupa_ui import Mostrar_roupas
from .cadastro_roupa_ui import CadastroRoupa
# from ..Template.adm_ui import AdmUI
from ..View.combinacao_view import CombinacaoView

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
        section = st.sidebar.selectbox("Menu", ["Home", "Armário", "Cadastro de Roupa", "Combinações"])

        if section == "Home":
            cls.__home()
        elif section == "Armário":
            cls.__armario()
        elif section == "Cadastro de Roupa":
            cls.__cadastro_roupa()
        elif section == "Combinações":
            cls.__combinacao()

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

    @classmethod
    def __combinacao(cls):
        st.markdown("<h1 style='text-align: center;'>Área de Combinações</h1>", unsafe_allow_html=True)
        st.header("Sugestões de Combinações")
        id_cliente = st.session_state.user.id
        
        # Campo de entrada para a mensagem
        mensagem = st.text_input("Digite sua mensagem", key="mensagem_combinacao")
        
        # Botão para buscar a resposta
        if st.button("Buscar Combinação"):
            if mensagem.strip():  # Verifica se a mensagem não está vazia
                with st.spinner("Gerando combinação..."):  # Mostra um spinner enquanto a requisição está em andamento
                    try:
                        resposta = CombinacaoView.obter_resposta(mensagem, id_cliente)
                        st.success("Combinação gerada com sucesso!")
                        st.write(resposta)  # Exibe a resposta na interface
                    except Exception as e:
                        st.error(f"Erro ao gerar combinação: {e}")
            else:
                st.warning("Por favor, digite uma mensagem antes de buscar a combinação.")