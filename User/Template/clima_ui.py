import streamlit as st
from ..View.clima_view import ClimaView

class Mostrar_clima:
    @classmethod
    def run(cls):
        cidade = st.text_input("Digite o nome da cidade:")
        if st.button("Buscar Clima"):
            clima_data = ClimaView.clima_info(cidade)
            
            if isinstance(clima_data, dict):  # Se retornou os dados do clima
                st.subheader(f"Clima em {clima_data['cidade']}, {clima_data['pais']}")
                st.write(f"🕒 **Última atualização:** {clima_data['data']}")
                st.write(f"🌤️ **Clima:** {clima_data['clima']}")
                st.write(f"🌡️ **Temperatura:** {clima_data['temperatura']}°C")
                st.write(f" **Sensação Térmica:** {clima_data['sensacao_termica']}°C")
                st.write(f" **Período:** {clima_data['periodo']}")
            else:
                st.warning(clima_data)