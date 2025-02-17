package Adm.Models.src;

import java.util.HashMap;
import java.util.Map;

public class Roupa implements Inter {
  private int id;
  private String nome_roupa;
  private String cor;
  private int id_tipo;
  private String detalhes;
  private int id_cliente;

  public Roupa(int id, String nome_roupa, String cor, int id_tipo, String detalhes, int id_cliente) {
    setId(id);
    setNome_roupa(nome_roupa);
    setCor(cor);
    setId_tipo(id_tipo);
    setDetalhes(detalhes);
    setId_cliente(id_cliente);
  }
  
  public Map<String, Object> toDict() {
    Map<String, Object> dict = new HashMap<>();
    dict.put("id", this.id);
    dict.put("nome_roupa", this.nome_roupa);
    dict.put("cor", this.cor);
    dict.put("id_tipo", this.id_tipo);
    dict.put("detalhes",this.detalhes);
    dict.put("id_cliente",this.id_cliente);
    return dict;
}

  @Override
  public String toString() {
      return "Item{" +
              "id=" + this.id +
              ", nome_roupa=" + this.nome_roupa +
              ", cor=" + this.cor +
              ", id_tipo=" + this.id_tipo +
              ", detalhes=" + this.detalhes +
              "id_cliente" + this.id_cliente;
  }

  public void setId(int id) {
    if (id >= 0) {
      this.id = id;
    } else {
      throw new IllegalArgumentException("ID inválido");
    }
  }

  public void setNome_roupa(String nome_roupa) {
    if (nome_roupa != null) {
      this.nome_roupa = nome_roupa;
    } else {
      throw new IllegalArgumentException("Nome inválido");
    }
  }

  public void setCor(String cor) {
    if (cor != null) {
      this.cor = cor;
    } else {
      throw new IllegalArgumentException("Cor inválida");
    }
  }

  public void setId_tipo(int id_tipo) {
    if (id_tipo >= 0) {
      this.id_tipo = id_tipo;
    } else {
      throw new IllegalArgumentException("Tipo inválido");
    }
  }

  public void setDetalhes(String detalhes) {
    if (detalhes != null) {
      this.detalhes = detalhes;
    } else {
      throw new IllegalArgumentException("Formato dos detalhes inválido");
    }
  }

  public void setId_cliente(int id_cliente) {
    if (id_cliente >= 0) {
      this.id_cliente = id_cliente;
    } else {
      throw new IllegalArgumentException("id cliente na área roupa inválido");
    }
  }

  public int getId() {
    return this.id;
  }

  public String getNome_roupa() {
    return this.nome_roupa;
  }

  public String getCor() {
    return this.cor;
  }

  public int getId_tipo() {
    return this.id_tipo;
  }

  public String getDetalhes() {
    return this.detalhes;
  }

  public int getId_cliente() {
    return this.id_cliente;
  }
}