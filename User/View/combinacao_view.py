import google.generativeai as genai
from ..Models.roupa import Roupa, Roupas
from ..Models.combinacao import Combinacao, Combinacoes

class CombinacaoView:
    @staticmethod
    def obter_resposta(temperatura: str, sensacao_termica: str, id_cliente: int):
        if not temperatura or not sensacao_termica:
            return "Informações de temperatura e sensação térmica são necessárias."

        genai.configure(api_key="AIzaSyB_W0Q1SLRZ2bs_TM3BoKgfzD11FOMXEoU")

        try:
            model = genai.GenerativeModel('gemini-pro')

            roupas_usuario = Roupas.listar()
            roupas_usuario = [roupa for roupa in roupas_usuario if roupa.id_cliente == id_cliente]

            if not roupas_usuario:
                return "Você não possui roupas cadastradas. Adicione roupas para receber recomendações."

            # Cria o prompt usando temperatura e sensação térmica
            prompt = (
                f"Com base na temperatura de {temperatura}°C e sensação térmica de {sensacao_termica}°C, "
                f"recomende combinações de roupas usando as seguintes peças:\n"
                f"{', '.join([f'{roupa.nome_roupa} ({roupa.cor})' for roupa in roupas_usuario])}.\n"
                "Se faltar alguma peça essencial, sugira a compra de uma peça adequada."
            )

            response = model.generate_content(prompt)
            recomendacao = response.text

            # Processa a resposta da IA para extrair roupas recomendadas
            ids_recomendados = []
            for roupa in roupas_usuario:
                # Verifica se o nome ou a cor da roupa está na recomendação
                if roupa.nome_roupa.lower() in recomendacao.lower() or roupa.cor.lower() in recomendacao.lower():
                    ids_recomendados.append(roupa.id)

            # Cria uma nova combinação apenas com os IDs das roupas recomendadas
            nova_combinacao = Combinacao(
                id=0,  # O ID será gerado automaticamente
                clima=f"{temperatura}°C (Sensação: {sensacao_termica}°C)",
                id_itens_roupas=ids_recomendados,  # Usa apenas os IDs recomendados
                id_cliente=id_cliente
            )
            Combinacoes.inserir(nova_combinacao)

            return recomendacao
        except Exception as e:
            return f"Erro ao obter resposta do Gemini: {e}"