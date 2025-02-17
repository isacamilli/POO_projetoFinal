package Adm.Models.src;

import java.util.HashMap;
import java.util.Map;

public class Local implements Inter {
  private int id;
  private String cidade;

  public Local(int id, String cidade) {
    setId(id);
    setCidade(cidade);
  }

  @Override
  public String toString() {
    return "Local:"+
      "id=" + this.id +
      ", cidade=" + this.cidade;
  }

  public Map<String, Object> toDict() {
    Map<String, Object> dict = new HashMap<>();
    dict.put("id", this.id);
    dict.put("cidade", this.cidade);
    return dict;
}

  public void setId(int id) {
    if (id >= 0) {
      this.id = id;
    } else {
      throw new IllegalArgumentException("ID inválido");
    }
  }

  public void setCidade(String cidade) {
    if (cidade instanceof String) {
      this.cidade = cidade;
    } else {
      throw new IllegalArgumentException("Cidade inválida");
    }
  }

  public int getId(){
    return this.id;
  }

  public String getCidade() {
    return this.cidade;
  }
}