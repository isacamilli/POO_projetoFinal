using System;
using System.Collections.Generic;
using System.IO;
using Newtonsoft.Json;
using System.Net.Http;
using System.Threading.Tasks;

public class PeriodoClima
{
    private int id;
    private string cidade;
    private string clima;
    private DateTime data;
    private string pais;
    private float temperatura;
    private string periodo;
    private float sensacaoTermica;

    public PeriodoClima(int id, string cidade)
    {
        setId(id);
        setCidade(cidade);
    }

    public override string ToString()
    {
        return $"Periodo_clima:
                  id={this.id} 
                  , cidade={this.cidade}";
    }

    public Dictionary<string, object> ToDict()
        {
            return new Dictionary<string, object>
            {
                { "id", periodoClima.Id },
                { "cidade", periodoClima.Cidade },
                { "pais", periodoClima.Pais },
                { "data", periodoClima.Data.ToString("dd/MM/yyyy HH:mm") },
                { "clima", periodoClima.Clima },
                { "periodo", periodoClima.Periodo },
                { "temperatura", periodoClima.Temperatura },
                { "sensacao_termica", periodoClima.SensacaoTermica }
            };
        }

    public void setId(int id)
    {
        if (id >= 0)
        {
            this.id = id;
        }
        else
        {
            throw new ArgumentException("ID clima inválido");
        }
    }

    public void setCidade(string cidade)
    {
        if (!string.IsNullOrEmpty(cidade))
        {
            this.cidade = cidade;
        }
        else
        {
            throw new ArgumentException("Cidade inválida");
        }
    }

    public int getId() => this.id;
    public string getCidade() => this.cidade;
    public string getClima() => this.clima;
    public DateTime getData() => this.data;
    public string getPais() => this.pais;
    public float getTemperatura() => this.temperatura;
    public string getPeriodo() => this.periodo;
    public float getSensacaoTermica() => this.sensacaoTermica;

    public async Task ClimaCidadeAsync()
    {
        string url = $"http://api.openweathermap.org/data/2.5/weather?q={Cidade}&appid=c5c2e778103223f1d989ac03ad6fcaee&units=metric&lang=pt_br";

        using (HttpClient client = new HttpClient())
        {
            HttpResponseMessage resposta = await client.GetAsync(url);

            if (resposta.IsSuccessStatusCode)
            {
                var dados = JsonConvert.DeserializeObject<Dictionary<string, object>>(await resposta.Content.ReadAsStringAsync());
                var sys = JsonConvert.DeserializeObject<Dictionary<string, object>>(dados["sys"].ToString());
                var weather = JsonConvert.DeserializeObject<List<Dictionary<string, object>>>(dados["weather"].ToString());
                var main = JsonConvert.DeserializeObject<Dictionary<string, object>>(dados["main"].ToString());

                this.pais = sys["country"].ToString();
                this.clima = weather[0]["description"].ToString();
                this.temperatura = Convert.ToSingle(main["temp"]);
                this.sensacaoTermica = Convert.ToSingle(main["feels_like"]);
                this.data = DateTime.Now;
                this.periodo = DeterminarPeriodo();
            }
            else
            {
                clima = "indisponível";
                temperatura = -1;
                sensacaoTermica = -1;
                data = DateTime.MinValue;
                periodo = "indisponível";
            }
        }
    }

    private string DeterminarPeriodo()
    {
        int mes = data.Month;

        if (mes == 12 || mes == 1 || mes == 2)
            return "Inverno";
        if (mes >= 3 && mes <= 5)
            return "Primavera";
        if (mes >= 6 && mes <= 8)
            return "Verão";
        return "Outono";
    }
}



