import google.generativeai as genai
from ..Models.roupa import Roupa, Roupas
from ..Models.combinacao import Combinacao, Combinacoes

class CombinacaoView:
    @staticmethod
    def obter_resposta(temperatura: str, id_cliente: int):
        if not temperatura:
            return "Digite uma temperatura para receber recomendações."

        genai.configure(api_key="AIzaSyB_W0Q1SLRZ2bs_TM3BoKgfzD11FOMXEoU")

        try:
            model = genai.GenerativeModel('gemini-pro')

            roupas_usuario = Roupas.listar()
            roupas_usuario = [roupa for roupa in roupas_usuario if roupa.id_cliente == id_cliente]

            if not roupas_usuario:
                return "Você não possui roupas cadastradas. Adicione roupas para receber recomendações."

            prompt = (
                f"Com base na temperatura de {temperatura}°C, recomende combinações de roupas usando as seguintes peças:\n"
                f"{', '.join([f'{roupa.nome_roupa} ({roupa.cor})' for roupa in roupas_usuario])}.\n"
                "Se faltar alguma peça essencial, sugira a compra de uma peça adequada."
            )

            response = model.generate_content(prompt)
            recomendacao = response.text

            # Extrai os IDs das roupas usadas na combinação
            ids_roupas = [roupa.id for roupa in roupas_usuario]

            # Cria uma nova combinação com os IDs das roupas, clima e ID do cliente
            nova_combinacao = Combinacao(
                id=0,
                clima=temperatura,
                id_itens_roupas=ids_roupas,
                id_cliente=id_cliente
            )
            Combinacoes.inserir(nova_combinacao)

            return recomendacao
        except Exception as e:
            return f"Erro ao obter resposta do Gemini: {e}"