public class Combinacao implements Inter{
  private int id;
  private String clima;
  private int id_itens_roupas;

  public Combinacao(int id, String clima, int id_itens_roupas) {
    this.setId(id);
    this.setClima(clima);
    this.setIdItens_roupas(id_itens_roupas);
  }

  @Override
  public String toString() {
    return String.format("%d - %s - %d", id, clima, id_itens_roupas);
  }

  public void setId(int id) {
    if (id >= 0) {
      this.id = id;
    } else {
      throw new IllegalArgumentException("ID combinação inválido");
    }
  }

  public void setClima(String clima) {
    if (clima != null) {
      this.clima = clima;
    } else {
      throw new IllegalArgumentException("clima combinação inválido");
    }
  }

  public void setIdItens_roupas(int id_itens_roupas) {
    if (id_itens_roupas >= 0) {
      this.id_itens_roupas = id_itens_roupas;
    } else {
      throw new IllegalArgumentException("id item_roupa area combinação inválida");
    }
  }

  public int getId() {
    return this.id;
  }

  public String getClima() {
    return this.clima;
  }

  public int getIdItens_roupas() {
    return this.id_itens_roupas;
  }
}