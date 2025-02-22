using Adm.View;

namespace Adm.Templates
{
    public class Login_UI(){
        public static int menu_cadastro(){
            Console.WriteLine("\nDeseja se registrar ou cadastrar um novo usuário?");
            Console.WriteLine("\n1 - Registrar-se");
            Console.WriteLine("2 - Cadastrar-se");
            Console.WriteLine("0 - Sair do sistema");

            Console.Write("\nDigite aqui: ");

            int numero = 0;

            while (!int.TryParse(Console.ReadLine(), out numero) || numero > 3)
            {
                Console.Write("\nEntrada inválida! Digite um número entre as opções: ");
            }

            return numero;
        }

        public static bool registro(){
            Console.WriteLine("\n------------- Tela de registro -------------");

            Console.Write("\nDigite o nome ou email: ");
            string nome = Console.ReadLine(); 

            Console.Write("Digite a senha: ");
            string senha = Console.ReadLine();

            bool entrada = Login_view.confEntrada(nome,senha);

            return entrada;
        }

        public static bool cadastro(){
            Console.WriteLine("\n------------- Tela de cadastro -------------");

            Console.Write("\nInsira o nome de usuario desejado: ");
            string nome = Console.ReadLine(); 

            Console.Write("Digite o email: ");
            string email = Console.ReadLine();
            
            Console.Write("Digite o fone(só números): ");
            string fone = Console.ReadLine();
            
            Console.Write("Digite o senha: ");
            string senha = Console.ReadLine();

            bool entrada = Login_view.CadastroCliente(nome,email,fone,senha);

            return entrada;
        }

    }
}