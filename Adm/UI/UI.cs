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

        // autenticar o login
        LoginView.LoginAuthentication(usuario, senha);
    }

    private static void Adm()
    {
        Console.Clear();
        Console.WriteLine(" Cloud Wear");
        Console.WriteLine("Bem-vindo ao Cloud Wear!");

        // Lógica para exibir as opções do cliente
        Console.WriteLine("1 - Visualizar roupas");
        Console.WriteLine("2 - Gerenciar guarda-roupa");
        Console.WriteLine("3 - Sair");

        string opcao = Console.ReadLine();

        switch (opcao)
        {
            case "1":
                VisualizarRoupas();
                break;
            case "2":
                GerenciarGuardaRoupa();
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
        // roupas do cliente
        Console.WriteLine("Roupas:");

    }

    private static void GerenciarGuardaRoupa()
    {
        // guarda-roupa do cliente
        Console.WriteLine("Guarda-roupa:");

    }

    private static void Sair()
    {
        // Lógica para sair do sistema
        Console.WriteLine("Saindo do sistema...");
        Environment.Exit(0);
    }
}