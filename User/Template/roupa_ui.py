import streamlit as st
from ..View.roupa_view import RoupaView

class Mostrar_roupas:
    @staticmethod
    def run():
        id_cliente = st.session_state.user.id
        
        # Obtém as roupas organizadas por tipo
        roupas_por_tipo = RoupaView.armario(id_cliente)
        
        if isinstance(roupas_por_tipo, str):
            st.info(roupas_por_tipo)  # Exibe uma mensagem se não houver roupas
        else:
            tipos_roupas = list(roupas_por_tipo.keys())
            
            # Centraliza o selectbox na tela
            col1, col2, col3 = st.columns([1, 2, 1])  # Cria 3 colunas (a do meio é mais larga)
            with col2:
                tipo_selecionado = st.selectbox("Selecione o tipo de roupa", tipos_roupas)
            
            # Obtém a descrição e as roupas correspondentes ao tipo selecionado
            descricao, roupas = roupas_por_tipo[tipo_selecionado]
            
            st.subheader(f"{tipo_selecionado}")
            st.markdown(f"{descricao}")
            
            for roupa in roupas:
                with st.expander(roupa.nome_roupa):
                    st.text(f"Cor: {roupa.cor}")
                    st.text(f"Detalhes: {roupa.detalhes}")
                    
                    if st.button(f"Excluir", key=f"excluir_{roupa.id}"):
                        if RoupaView.excluir_roupa(roupa.id):
                            st.success(f"Roupa '{roupa.nome_roupa}' excluída com sucesso!")
                            st.rerun()
                        else:
                            st.error("Erro ao excluir a roupa.")