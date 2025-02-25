import streamlit as st
from ..View.clima_view import ClimaView
from ..View.combinacao_view import CombinacaoView

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

                # Exibir combinações de roupas com base na temperatura
                st.markdown("<h2 style='text-align: center;'>Sugestões de Combinações</h2>", unsafe_allow_html=True)
                with st.spinner("Gerando combinações..."):
                    try:
                        id_cliente = st.session_state.user.id
                        # Passa apenas a temperatura e a sensação térmica
                        resposta = CombinacaoView.obter_resposta(
                            temperatura=clima_data['temperatura'],
                            sensacao_termica=clima_data['sensacao_termica'],
                            id_cliente=id_cliente
                        )
                        st.success("Combinações geradas com sucesso!")
                        st.write(resposta)  # Exibe a resposta na interface
                    except Exception as e:
                        st.error(f"Erro ao gerar combinações: {e}")
            else:
                st.warning(clima_data)