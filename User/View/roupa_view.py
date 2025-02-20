import streamlit as st
from ..Models.roupa import Roupa, Roupas

class RoupaView:

    @staticmethod
    def armario(id_cliente):
        armario = []

        # olha se tem alguém logado
        if "user" in st.session_state and st.session_state.user['id'] == id_cliente:
            for roupa in Roupas.listar():
                if roupa.id_cliente == id_cliente:
                    armario.append(roupa)

        if not armario:
            st.info("Nenhuma roupa cadastrada no armário.")
            return

        # separa por tipo
        roupas_por_tipo = {}
        for roupa in armario:
            if roupa.id_tipo not in roupas_por_tipo:
                roupas_por_tipo[roupa.id_tipo] = []
            roupas_por_tipo[roupa.id_tipo].append(roupa)

        for tipo, roupas in roupas_por_tipo.items():
            st.subheader(f"Tipo {tipo}")
            for roupa in roupas:
                st.write(f"Nome: {roupa.nome_roupa}")
                st.write(f"Cor: {roupa.cor}")
                st.write(f"Detalhes: {roupa.detalhes}")
                st.markdown("---")


    @staticmethod
    def cadastrar_roupa(nome_roupa, cor, tipo: int, detalhes, id_Roupa: int, id_cliente: int):
        if nome_roupa and cor and tipo and detalhes:
            nova_roupa = Roupa(0, nome_roupa, cor, tipo, detalhes, id_Roupa, id_cliente)
            Roupas.inserir(nova_roupa)
            st.success("Roupa cadastrada com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos para cadastrar a roupa.")