package src;

import java.util.HashMap;
import java.util.Map;

public class Cliente implements Inter {
  private int id;
  private String nome;
  private String email;
  private String fone;
  private String senha;
  private boolean adm;

  public Cliente(int id, String nome, String email, String fone, String senha, boolean adm) {
    setId(id);
    setNome(nome);
    setEmail(email);
    setFone(fone);
    setSenha(senha);
    setAdm(adm);
  }

  // @Override
  // public String toString() {
  //   return String.format("%d - %s - %s - %s", id, nome, email, fone);
  // }

  public void setId(int id) {
    if (id < 0) {
      throw new IllegalArgumentException("id inválido");
    }
    this.id = id;
  }

  public void setNome(String nome) {
    if (nome == null || nome.isEmpty()) {
      throw new IllegalArgumentException("nome não pode ser vazio");
    }
    this.nome = nome;
  }

  public void setEmail(String email) {
    if (email == null || !email.getClass().equals(String.class)) {
      throw new IllegalArgumentException("Email inválido");
    }
    this.email = email;
  }

  public void setFone(String fone) {
    if (fone == null || fone.isEmpty()) {
      throw new IllegalArgumentException("fone não pode ser vazio");
    }
    this.fone = fone;
  }

  public void setSenha(String senha) {
    if (senha == null || senha.isEmpty()) {
      throw new IllegalArgumentException("senha não pode ser vazia");
    }
    this.senha = senha;
  }

  public void setAdm(boolean adm) {
    this.adm = adm;
  }

  public int getId() {
    return id;
  }

  public String getNome() {
    return nome;
  }

  public String getEmail() {
    return email;
  }

  public String getFone() {
    return fone;
  }

  public String getSenha() {
    return senha;
  }

  public boolean isAdm() {
    return adm;
  }

  public Map<String, Object> toDict() {
    Map<String, Object> dict = new HashMap<>();
    dict.put("id", this.id);
    dict.put("nome", this.nome);
    dict.put("email", this.email);
    dict.put("fone", this.fone);
    dict.put("senha",this.senha);
    dict.put("adm",this.senha);
    return dict;
}
  @Override
  public String toString() {
      return "Item{" +
              "id=" + id +
              ", nome=" + nome +
              ", email=" + email +
              ", fone=" + fone +
              ", senha=" + senha +
              "adm" + adm +
              '}';
  }
}
