package Adm.Models.src;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.HashMap;
import java.util.Map;

public class PeriodoClima implements Inter{
  private int id;
  private String cidade;
  private String pais;
  private String clima;
  private LocalDateTime data;
  private String periodo;
  private double temperatura;
  private double sensacaoTermica;

  public PeriodoClima(int id, String cidade) {
    setId(id);
    setCidade(cidade);
  }

  @Override
  public String toString() {
    return "Periodo_clima:" +
             "id=" + this.id +
             ", cidade=" + this.cidade;
  }

  public Map<String, Object> toDict() {
    Map<String, Object> dict = new HashMap<>();
    dict.put("id", this.id);
    dict.put("cidade", this.cidade);
    dict.put("pais", this.pais);
    dict.put("data", this.data.format(DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm")));
    dict.put("clima",this.clima);
    dict.put("periodo",this.periodo);
    dict.put("temperatura",this.temperatura);
    dict.put("sensacao_termica",this.sensacaoTermica);
    return dict;
}

  public void setId(int id){
    if (id > 0 ){
      this.id = id;
    }
    else{
      throw new IllegalArgumentException("id clima inválido");
    }
  }

  public void setCidade(String cidade) {
    if (cidade == null || cidade.isEmpty()) {
      throw new IllegalArgumentException("Cidade inválida");
    }
    this.cidade = cidade;
  }

  public int getId() {
    return this.id;
  }

  public String getCidade() {
    return this.cidade;
  }

  public String getClima() {
    return this.clima;
  }

  public LocalDateTime getData() {
    return this.data;
  }

  public String getPeriodo() {
    return this.periodo;
  }

  public void climaCidade() {
    String url = String.format(
        "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=c5c2e778103223f1d989ac03ad6fcaee&units=metric&lang=pt_br",
        this.cidade);
    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create(url))
        .GET()
        .build();

    try {
      HttpResponse<String> response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
      if (response.statusCode() == 200) {
        String dados = response.body();
        // Parse JSON
        this.pais = getJsonValue(dados, "sys.country");
        this.clima = getJsonValue(dados, "weather[0].description");
        this.temperatura = Double.parseDouble(getJsonValue(dados, "main.temp"));
        this.sensacaoTermica = Double.parseDouble(getJsonValue(dados, "main.feels_like"));
        this.data = LocalDateTime.now();
        this.periodo = determinarPeriodo();
      } else {
        this.clima = "indisponível";
        this.temperatura = Double.NaN;
        this.sensacaoTermica = Double.NaN;
        this.data = null;
        this.periodo = "indisponível";
      }
    } catch (IOException | InterruptedException e) {
      System.err.println("Erro ao consultar API: " + e.getMessage());
    }
  }

  private String getJsonValue(String json, String key) {
    int startIndex = json.indexOf(key) + key.length() + 4;
    int endIndex = json.indexOf(',', startIndex);
    return json.substring(startIndex, endIndex).trim().replaceAll("\"", "");
  }

  private String determinarPeriodo() {
    int mes = data.getMonthValue();
    if (mes >= 12 || mes <= 2)
      return "Inverno";
    else if (mes >= 3 && mes <= 5)
      return "Primavera";
    else if (mes >= 6 && mes <= 8)
      return "Verão";
    else
      return "Outono";
  }
}