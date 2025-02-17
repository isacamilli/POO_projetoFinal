import streamlit as st
from ..Models.clima import Periodo_Clima, Climas

class ClimaView:
    @classmethod
    def clima_info(cls, cidade: str):
        if not cidade:
            st.warning("Por favor, insira o nome de uma cidade.")
            return

        periodo_clima = Periodo_Clima(id=1, cidade=cidade)
        periodo_clima.clima_cidade()

        if periodo_clima.clima != "indisponível":
            st.subheader(f"Clima em {periodo_clima.cidade}, {periodo_clima.pais}")
            st.write(f"🕒 **Última atualização:** {periodo_clima.data}")
            st.write(f"🌤️ **Clima:** {periodo_clima.clima}")
            st.write(f"🌡️ **Temperatura:** {periodo_clima.temperatura}°C")
            st.write(f" **Sensação Térmica:** {periodo_clima.sensacao_termica}°C")
            st.write(f" **Período:** {periodo_clima.periodo}")

            Climas.salvar_clima(periodo_clima)
        else:
            st.error("❌ Não foi possível obter os dados climáticos. Verifique a cidade e tente novamente.")
