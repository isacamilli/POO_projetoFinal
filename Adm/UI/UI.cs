using System;
using Adm.Models;

public class UI
{
    public static void Run()
    {
        if (SessionState.Page == null)
        {
            SessionState.Page = "login";
        }

        if (SessionState.User == null)
        {
            SessionState.User = null;
        }

        Console.Title = "Cloud Wear";

        while (true)
        {
            switch (SessionState.Page)
            {
                case "home":
                    Cliente();
                    break;
                case "login":
                    Login();
                    break;
            }
        }
    }

    private static void Login()
    {
        Console.Clear();
        Console.WriteLine("🌤️ Cloud Wear");
        
        Console.WriteLine("\nEscolha uma opção:");
        Console.WriteLine("1 - Entrar");
        Console.WriteLine("2 - Cadastro");
        string opcao = Console.ReadLine();

        switch (opcao)
        {
            case "1":
                Entrar();
                break;
            case "2":
                Cadastro();
                break;
            default:
                Console.WriteLine("Opção inválida.");
                break;
        }
    }

    private static void Entrar()
    {
        Console.Clear();
        Console.WriteLine("🌤️ Cloud Wear");
        Console.WriteLine("\nAcesse sua conta");

        Console.Write("Nome de usuário ou Email: ");
        string usuario = Console.ReadLine();
        Console.Write("Senha: ");
        string senha = Console.ReadLine();

        // Chamada à view para autenticar o login
        LoginView.LoginAuthentication(usuario, senha);
    }

    private static void Cadastro()
    {
        Console.Clear();
        Console.WriteLine("🌤️ Cloud Wear");
        Console.WriteLine("\nCriar uma nova conta");

        Console.Write("Nome: ");
        string usuario = Console.ReadLine();
        Console.Write("Email: ");
        string email = Console.ReadLine();
        Console.Write("Telefone: ");
        string fone = Console.ReadLine();
        Console.Write("Senha: ");
        string senha = Console.ReadLine();

        // Chamada à view para registrar um novo usuário
        LoginView.RegisterAuthentication(usuario, email, fone, senha);
    }

    private static void Cliente()
    {
        Console.Clear();
        Console.WriteLine("🌤️ Cloud Wear");
        Console.WriteLine("\nMenu:");
        Console.WriteLine("1 - Home");
        Console.WriteLine("2 - Armário");
        Console.WriteLine("3 - Cadastro de Roupa");
        Console.WriteLine("4 - Sair");
        string opcao = Console.ReadLine();

        switch (opcao)
        {
            case "1":
                Home();
                break;
            case "2":
                Armario();
                break;
            case "3":
                CadastroRoupa();
                break;
            case "4":
                Sair();
                break;
            default:
                Console.WriteLine("Opção inválida.");
                break;
        }
    }

    private static void Home()
    {
        Console.Clear();
        Console.WriteLine("🌤️ Cloud Wear");
        Console.WriteLine("\nConfira o clima para escolher a combinação certa.");
    }

    private static void Armario()
    {
        Console.Clear();
        Console.WriteLine("🌤️ Cloud Wear");
        Console.WriteLine("\nRoupas no armário");

        // Adicione lógica para exibir roupas aqui
    }

    private static void CadastroRoupa()
    {
        Console.Clear();
        Console.WriteLine("🌤️ Cloud Wear");
        Console.WriteLine("\nCadastrar Nova Roupa");

        // Adicione lógica para cadastro de roupa aqui
    }

    private static void Sair()
    {
        SessionState.Page = "login";
        Console.Clear();
        Console.WriteLine("Deslogado com sucesso. Redirecionando para login...");
    }
}
