package Adm_java.Models.src;

public class teste {
  public static void main(String[] args){
    int id = 1;
    String nome = "isa";
    String email = "email@email.com";
    String tel = "1ylt56789";
    String senha = "02";
    boolean adm = true;
    Cliente cliente = new Cliente(id, nome, email, tel, senha, adm);
    Clientes clientes = new Clientes();
    clientes.inserir(cliente);
    Roupa roupa1 = new Roupa(1, "blusa", "preto", 2, "blusa fria", 1);
    Roupas roupas = new Roupas();
    roupas.inserir(roupa1);
  }
}