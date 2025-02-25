import streamlit as st

class AdmUI:
    @classmethod
    def run(cls):
        # Título centralizado
        st.markdown("<h1 style='text-align: center;'>🌤️ Cloud Wear</h1>", unsafe_allow_html=True)

        for _ in range(10):
            st.write("")

        st.markdown("<h2 style='text-align: center;'>Admin logado</h2>", unsafe_allow_html=True)

        if st.sidebar.button("❌ Sair"):
            st.session_state.page = 'login'
            st.rerun()