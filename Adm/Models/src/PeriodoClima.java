import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class PeriodoClima {
  private String cidade;
  private String pais;
  private String clima;
  private LocalDateTime data;
  private String periodo;
  private double temperatura;
  private double sensacaoTermica;

  public PeriodoClima(String cidade) {
    setCidade(cidade);
  }

  @Override
  public String toString() {
    return String.format(
        "Cidade: %s|%s - Data: %s - Clima: %s - Período: %s - Temperatura: %.2f°C - Sensação Térmica: %.2f°C",
        cidade, pais, data.format(DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm")), clima, periodo, temperatura,
        sensacaoTermica);
  }

  public void setCidade(String cidade) {
    if (cidade == null || cidade.isEmpty()) {
      throw new IllegalArgumentException("Cidade inválida");
    }
    this.cidade = cidade;
  }

  public String getCidade() {
    return cidade;
  }

  public String getClima() {
    return clima;
  }

  public LocalDateTime getData() {
    return data;
  }

  public String getPeriodo() {
    return periodo;
  }

  public void climaCidade() {
    String url = String.format(
        "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=c5c2e778103223f1d989ac03ad6fcaee&units=metric&lang=pt_br",
        cidade);
    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create(url))
        .GET()
        .build();

    try {
      HttpResponse<String> response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
      if (response.statusCode() == 200) {
        String dados = response.body();
        // Parse JSON
        pais = getJsonValue(dados, "sys.country");
        clima = getJsonValue(dados, "weather[0].description");
        temperatura = Double.parseDouble(getJsonValue(dados, "main.temp"));
        sensacaoTermica = Double.parseDouble(getJsonValue(dados, "main.feels_like"));
        data = LocalDateTime.now();
        periodo = determinarPeriodo();
      } else {
        clima = "indisponível";
        temperatura = Double.NaN;
        sensacaoTermica = Double.NaN;
        data = null;
        periodo = "indisponível";
      }
    } catch (IOException | InterruptedException e) {
      System.err.println("Erro ao consultar API: " + e.getMessage());
    }
  }

  private String getJsonValue(String json, String key) {
    int startIndex = json.indexOf(key) + key.length() + 2;
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