public class teste {
  public static void main(String[] args){
    int id = 1;
    String nome = "icaro";
    String email = "email@email.com";
    String tel = "123456789";
    String senha = "02";
    boolean adm = true;
    Cliente cliente = new Cliente(id, nome, email, tel, senha, adm);
    Clientes clientes = new Clientes();
    clientes.inserir(cliente);
  }
}