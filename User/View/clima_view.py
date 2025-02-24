from ..Models.clima import Periodo_Clima, Climas

class ClimaView:
    @classmethod
    def clima_info(cls, cidade: str):
        if not cidade:
            return "Por favor, insira o nome de uma cidade."

        periodo_clima = Periodo_Clima(id=1, cidade=cidade)
        periodo_clima.clima_cidade()

        if periodo_clima.clima != "indisponível":
            clima_data = {
                "cidade": periodo_clima.cidade,
                "pais": periodo_clima.pais,
                "data": periodo_clima.data,
                "clima": periodo_clima.clima,
                "temperatura": periodo_clima.temperatura,
                "sensacao_termica": periodo_clima.sensacao_termica,
                "periodo": periodo_clima.periodo
            }

            Climas.salvar_clima_em_json(periodo_clima)
            return clima_data
        else:
            return "❌ Não foi possível obter os dados climáticos. Verifique a cidade e tente novamente."

