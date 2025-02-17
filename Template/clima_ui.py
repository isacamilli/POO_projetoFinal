import streamlit as st
from User.View.clima_view import ClimaView

class Mostrar_clima:
    @classmethod
    def run(cls):
        cidade = st.text_input("Digite o nome da cidade:")
        if st.button("Buscar Clima"): ClimaView.clima_info(cidade)
        else: st.warning("Digite uma cidade")