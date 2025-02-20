using System;
using System.Linq;
using Adm.Models;  // Usando o namespace correto

public class LoginView
{
    public static void LoginAuthentication(string user, string password)
    {
        // Abrir os clientes a partir do arquivo
        var clientes = new Clientes();
        clientes.Abrir();

        foreach (var cliente in clientes.Listar())
        {
            if ((cliente.getEmail() == user || cliente.getNome() == user) && cliente.getSenha() == password)
            {
                if (cliente.isAdm())
                {
                    // Alterar página para admin (exemplo)
                    SessionState.Page = "admin";
                }
                else
                {
                    // Alterar página para home (exemplo)
                    SessionState.Page = "home";
                }

                SessionState.User = cliente;
                Console.WriteLine($"Bem-vindo, {cliente.getNome()}");
                return;
            }
        }

        Console.WriteLine("Email ou senha inválido!");
    }

    public static void RegisterAuthentication(string username, string userEmail, string telefone, string password)
    {
        var liberado = true;
        var clientes = new Clientes();
        clientes.Abrir();

        foreach (var cliente in clientes.Listar())
        {
            if (cliente.getEmail() == userEmail || cliente.getNome() == username)
            {
                liberado = false;
                Console.WriteLine("Usuário já existente");
            }
        }

        var usernamesInvalidos = new[] { "adm", "ADM", "Adm", "admin", "ADMIN", "Admin", "administrador", "ADMINISTRADOR", "Administrador" };
        if (usernamesInvalidos.Contains(username))
        {
            liberado = false;
            Console.WriteLine("Nome de usuário inapropriado");
        }

        if (telefone.Any(c => Char.IsLetter(c)))  // Verifica se o telefone contém letras
        {
            liberado = false;
            Console.WriteLine("Telefone não pode conter letras");
        }

        if (liberado)
        {
            var cliente = new Cliente(0, username, userEmail, telefone, password, false);
            clientes.Inserir(cliente);
            clientes.Salvar();
            Console.WriteLine("Usuário cadastrado com sucesso");
        }
    }
}
