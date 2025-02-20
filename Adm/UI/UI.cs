using System;
using System.Linq;
using Adm.Models;

public class UI
{
    public static void Run()
    {
        if (SessionState.Page == null)
        {
            SessionState.Page = "login";
        }

        Console.Title = "Cloud Wear";

        // Loop contínuo até que o usuário saia
        while (true)
        {
            switch (SessionState.Page)
            {
                case "home":
                    Adm();
                    break;
                case "login":
                    Login();
                    break;
                default:
                    Console.WriteLine("Página não encontrada.");
                    break;
            }
        }
    }

    private static void Login()
    {
        Console.Clear();
        Console.WriteLine(" Cloud Wear");
        Console.WriteLine("Acesse sua conta");

        Console.Write("Nome de usuário ou Email: ");
        string usuario = Console.ReadLine();
        Console.Write("Senha: ");
        string senha = Console.ReadLine();

        // Chama o método de autenticação
        LoginView.LoginAuthentication(usuario, senha);
    }

    private static void Adm()
    {
        Console.Clear();
        Console.WriteLine(" Cloud Wear");
        Console.WriteLine("Bem-vindo ao Cloud Wear admin!");

        // Menu de opções para o admin
        Console.WriteLine("1 - Visualizar usuários");
        Console.WriteLine("2 - Visualizar roupas");
        Console.WriteLine("3 - Sair");

        string opcao = Console.ReadLine();

        switch (opcao)
        {
            case "1":
                VisualizarUser();
                break;
            case "2":
                VisualizarRoupas();
                break;
            case "3":
                Sair();
                break;
            default:
                Console.WriteLine("Opção inválida.");
                break;
        }
    }

    private static void VisualizarRoupas()
    {
        // Aqui, você deve carregar e exibir as roupas cadastradas
        Console.WriteLine("Roupas cadastradas:");
        var roupas = Roupas.Listar();  // Listando as roupas
        foreach (var roupa in roupas)
        {
            Console.WriteLine($"Nome: {roupa.getNome()}, Cor: {roupa.getCor()}, Tipo: {roupa.getTipo()}");
        }
    }

    private static void VisualizarUser()
    {
        // Aqui, você deve carregar e exibir os usuários cadastrados
        Console.WriteLine("Usuários cadastrados:");
        var clientes = Clientes.Listar();  // Listando os clientes
        foreach (var cliente in clientes)
        {
            Console.WriteLine($"Nome: {cliente.getNome()}, Email: {cliente.getEmail()}");
        }
    }

    private static void Sair()
    {
        // Lógica para sair do sistema
        Console.WriteLine("Saindo do sistema...");
        SessionState.Page = null;  // Resetando a página para null
        break;  // Encerra o loop principal
    }
}

// Simulação de SessionState (se necessário)
public static class SessionState
{
    public static string Page { get; set; }
    public static Cliente User { get; set; }
}