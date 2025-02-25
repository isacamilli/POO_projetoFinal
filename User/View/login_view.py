import streamlit as st
from ..Models.cliente import Cliente, Clientes

class Login_View:
    @staticmethod
    def login_authentication(user: str, password: str):
        for cliente in Clientes.listar():
            if (cliente.email == user or cliente.nome == user.lower()) and cliente.senha == password:
                if cliente.adm:
                    st.session_state.page = 'admin'
                    st.rerun()
                else:
                    st.session_state.page = 'home'
                    st.session_state.user = cliente
                    st.success(f"Bem-vindo, {cliente.nome}")
                    st.rerun()
                return
            
        st.error("Email ou senha inválido!")

    @staticmethod
    def register_authentication(Username: str, User_email: str, telefone: str, password: str, adm: bool = False):
        liberado = True
        for cliente in Clientes.listar():
            if cliente.email == User_email or cliente.nome == Username:
                liberado = False
                st.error("Usuário já existente")

        if Username in ["adm", "ADM", "Adm", "admin", "ADMIN", "Admin", "administrador", "ADMINISTRADOR", "Administrador"]:
            liberado = False
            st.error("Nome de usuário inapropriado")

        if any(65 <= ord(c) <= 90 or 97 <= ord(c) <= 122 for c in telefone):    #ord
            liberado = False
            st.error("Telefone não pode conter letras")

        if liberado:
            c = Cliente(
                id=0,
                nome=Username.lower(),
                email=User_email,
                fone=telefone,
                senha=password,
                adm=adm
            )
            Clientes.inserir(c)
            st.success("Usuário cadastrado com sucesso")

    @staticmethod
    def verificar_admin_existente(nome: str, email: str) -> bool:
        for cliente in Clientes.listar():
            if (cliente.nome == nome.lower() or cliente.email == email) and cliente.adm:
                return True
        return False
    
    @staticmethod
    def criar_adm(Username: str, User_email: str, telefone: str, password: str, adm: bool = True):
        c = Cliente(
            id=0,
            nome=Username.lower(),
            email=User_email,
            fone=telefone,
            senha=password,
            adm=adm
        )
        Clientes.inserir(c)