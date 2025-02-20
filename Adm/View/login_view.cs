using System;
using System.Linq;
using Adm.Models;  // Usando o namespace correto

namespace Adm.View
{
    public class LoginView
    {
        // Método para autenticação do login
        public static void LoginAuthentication(string user, string password)
        {
            // Abrir os clientes a partir do arquivo
            var clientes = new Clientes();
            clientes.Abrir();

            // Procurar o cliente correspondente ao nome ou email
            var cliente = clientes.Listar()
                                  .FirstOrDefault(c => (c.getEmail() == user || c.getNome() == user) && c.getSenha() == password);

            if (cliente != null)
            {
                // Definir a página conforme o tipo de usuário
                if (cliente.isAdm())
                {
                    SessionState.Page = "admin";
                }
                else
                {
                    SessionState.Page = "home";
                }

                // Salvar o cliente na sessão
                SessionState.User = cliente;
                Console.WriteLine($"Bem-vindo, {cliente.getNome()}");
            }
            else
            {
                Console.WriteLine("Email ou senha inválido!");
            }
        }

        // Método para cadastro de um novo usuário
        public static void RegisterAuthentication(string username, string userEmail, string telefone, string password)
        {
            bool liberado = true;
            var clientes = new Clientes();
            clientes.Abrir();

            // Verificar se o usuário ou email já existe
            if (clientes.Listar().Any(c => c.getEmail() == userEmail || c.getNome() == username))
            {
                liberado = false;
                Console.WriteLine("Usuário já existente");
            }

            // Verificar se o nome de usuário é inválido
            var usernamesInvalidos = new[] { "adm", "ADM", "Adm", "admin", "ADMIN", "Admin", "administrador", "ADMINISTRADOR", "Administrador" };
            if (usernamesInvalidos.Contains(username))
            {
                liberado = false;
                Console.WriteLine("Nome de usuário inapropriado");
            }

            // Verificar se o telefone contém letras (uso de Regex para ser mais robusto)
            if (telefone.Any(c => !Char.IsDigit(c)))
            {
                liberado = false;
                Console.WriteLine("Telefone não pode conter letras");
            }

            // Caso esteja liberado, realizar o cadastro
            if (liberado)
            {
                var cliente = new Cliente(0, username, userEmail, telefone, password, false);
                clientes.Inserir(cliente);
                clientes.Salvar();
                Console.WriteLine("Usuário cadastrado com sucesso");
            }
        }
    }

    // Estrutura para manter o estado da sessão
    public static class SessionState
    {
        public static string Page { get; set; }
        public static Cliente User { get; set; }
    }
}
