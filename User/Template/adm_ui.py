import streamlit as st

class AdmUI:
    @classmethod
    def adm(cls):
        st.write("adm")
        section = st.sidebar.selectbox("Menu Adm",("Clientes", "Roupas"))

        match section:
            case "Clientes":
                st.header("Clientes ativos")
                st.write("---")

            case "Roupas":
                st.header("Clientes ativos")
                st.write("---")


        if st.sidebar.button("❌ Sair"):
            st.session_state.page = 'login'
            st.rerun()