public class Tipo_roupa implements Inter{
  private int id;
  private String nome;
  private String descricao;

  public Tipo_roupa(int id, String nome, String descricao) {
    setId(id);
    setNome(nome);
    setDescricao(descricao);
  }

  @Override
  public String toString() {
    return String.format("%d - %s - %s", id, nome, descricao);
  }

  public void setId(int id) {
    if (id >= 0) {
      this.id = id;
    } else {
      throw new IllegalArgumentException("ID tipo_roupa inválido");
    }
  }

  public void setNome(String nome) {
    if (nome != null) {
      this.nome = nome;
    } else {
      throw new IllegalArgumentException("Nome tipo_roupa inválido");
    }
  }

  public void setDescricao(String descricao) {
    if (descricao != null) {
      this.descricao = descricao;
    } else {
      throw new IllegalArgumentException("Descrição inválida");
    }
  }

  public int getId() {
    return this.id;
  }

  public String getNome() {
    return this.nome;
  }

  public String getDescricao() {
    return this.descricao;
  }
}