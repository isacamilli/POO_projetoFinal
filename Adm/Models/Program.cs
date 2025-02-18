class Program
{
    static void Main(string[] args)
    {
        // Criando um cliente com valores de exemplo
        Cliente cliente1 = new Cliente(
            id: 1, 
            nome: "Ana Souza", 
            email: "ana.souza@email.com", 
            fone: "(11) 91234-5678", 
            senha: "senha123", 
            adm: true);

        Cliente cliente2 = new Cliente(
            id: 2, 
            nome: "Carlos Silva", 
            email: "carlos.silva@email.com", 
            fone: "(21) 99876-5432", 
            senha: "senha456", 
            adm: false);

        // Exibindo informações dos clientes
        Console.WriteLine($"Cliente 1: {cliente1.Nome}, {cliente1.Email}, {cliente1.Fone}, Admin: {cliente1.Adm}");
        Console.WriteLine($"Cliente 2: {cliente2.Nome}, {cliente2.Email}, {cliente2.Fone}, Admin: {cliente2.Adm}");
    }
}
