using System;
using Adm.Models;  // Certifique-se de que o namespace está correto

class Program
{
    static void Main(string[] args)
    {

        Clientes clientesManager = new Clientes();

        // Criando um cliente com valores de exemplo
        Cliente cliente1 = new Cliente(
            id: 0, 
            nome: "Ana Souza", 
            email: "ana.souza@email.com", 
            fone: "(11) 91234-5678", 
            senha: "senha123", 
            adm: true);

        Cliente cliente2 = new Cliente(
            id: 0, 
            nome: "Carlos Silva", 
            email: "carlos.silva@email.com", 
            fone: "(21) 99876-5432", 
            senha: "senha456", 
            adm: false);

            clientesManager.Inserir(cliente1);
            clientesManager.Inserir(cliente2);

        // Exibindo informações dos clientes
        Console.WriteLine($"Cliente 1: {cliente1.GetNome()}, {cliente1.GetEmail()}, {cliente1.GetFone()}, Admin: {cliente1.IsAdm()}");
        Console.WriteLine($"Cliente 2: {cliente2.GetNome()}, {cliente2.GetEmail()}, {cliente2.GetFone()}, Admin: {cliente2.IsAdm()}");
    }
}
