package Adm.Models.src;

public class Main {
    public static void main(String[] args) {
        // Criando um objeto Cliente
        Cliente cliente = new Cliente(1, "João", "joao@email.com", "123456789", "senha123", true);
        
        // Exibindo os dados do cliente usando o método toString()
        System.out.println(cliente);
        
        // Exibindo o cliente em formato de dicionário
       // System.out.println(cliente.toString());
    }
}
