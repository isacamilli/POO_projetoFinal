public class Roupa {
  private int id;
  private String nomeRoupa;
  private String cor;
  private int idTipo;
  private String detalhes;
  private int idCliente;

  public Roupa(int id, String nomeRoupa, String cor, int idTipo, String detalhes, int idCliente) {
    this.setId(id);
    this.setNomeRoupa(nomeRoupa);
    this.setCor(cor);
    this.setIdTipo(idTipo);
    this.setDetalhes(detalhes);
    this.setIdCliente(idCliente);
  }

  @Override
  public String toString() {
    return String.format("%d - %s - %s - %d - %s - %d", id, nomeRoupa, cor, idTipo, detalhes, idCliente);
  }

  public void setId(int id) {
    if (id >= 0) {
      this.id = id;
    } else {
      throw new IllegalArgumentException("ID inválido");
    }
  }

  public void setNomeRoupa(String nomeRoupa) {
    if (nomeRoupa != null) {
      this.nomeRoupa = nomeRoupa;
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

  public void setIdTipo(int idTipo) {
    if (idTipo >= 0) {
      this.idTipo = idTipo;
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

  public void setIdCliente(int idCliente) {
    if (idCliente >= 0) {
      this.idCliente = idCliente;
    } else {
      throw new IllegalArgumentException("id cliente na área roupa inválido");
    }
  }

  public int getId() {
    return id;
  }

  public String getNomeRoupa() {
    return nomeRoupa;
  }

  public String getCor() {
    return cor;
  }

  public int getIdTipo() {
    return idTipo;
  }

  public String getDetalhes() {
    return detalhes;
  }

  public int getIdCliente() {
    return idCliente;
  }
}