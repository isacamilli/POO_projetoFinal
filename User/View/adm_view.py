import streamlit as st
from ..Models.cliente import Clientes
from ..Models.roupa import Roupas

class AdmView:
    @staticmethod
    def listar_clientes():
        return Clientes.listar()
    
    @staticmethod
    def alterar_adm(client):
        client.set_adm(not(client.adm))
        Clientes.salvar()

    @classmethod
    def listar_roupas():
        return Roupas.listar()

    @classmethod
    def listar_roupas_id():
        roupas = AdmView.listar_roupas()
        roupas_por_cliente = {}

        for roupa in roupas:
            if roupa["id_cliente"] not in roupas_por_cliente:
                roupas_por_cliente["id_cliente"] = []
            roupas_por_cliente["id_cliente"].append(roupa)