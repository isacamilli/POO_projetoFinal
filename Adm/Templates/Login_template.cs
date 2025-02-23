using Adm.View;

namespace Adm.Templates
{
    public class Login_UI{
        public static void menu_cadastro(){

            int numero = 1;

            while (numero != 0){
                Console.WriteLine("\n-------------------------------------");
                Console.WriteLine("\nDeseja se registrar ou cadastrar um novo usuário?");
                Console.WriteLine("\n1 - Registrar-se");
                Console.WriteLine("2 - Cadastrar-se");
                Console.WriteLine("0 - Sair do sistema");

                Console.Write("\nDigite aqui: ");

                if (int.TryParse(Console.ReadLine(), out numero))
                {
                    switch (numero)
                    { 
                        case 0:
                            Console.WriteLine("\nSaindo do sistema....");
                            break;

                        case 1:
                            bool  entrar_sistema = Login_UI.registro();
                
                            if (entrar_sistema){
                            numero = Cliente_UI.Menu_cliente();
                            }
                            
                            break;

                        case 2:
                            Login_UI.cadastro();
                            break;
                                        
                        default:
                            Console.WriteLine("\nEntrada inválida! Digite um número entre as opções.");
                            break;
                    }
                }
                else
                {
                    Console.WriteLine("\nEntrada inválida! Digite um número.");
                    numero = 1;
                }

            }
            
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

            // verificar numero

            bool verifNum = false;
            string fone = "";
            
            while (!verifNum){

                Console.Write("Digite o fone(só números): ");
                fone = Console.ReadLine();

                verifNum = fone.All(char.IsDigit);

                if (!verifNum){
                    Console.WriteLine("O número não pode conter caracteres");
                }
                else{
                    break;
                }

            }
            
            Console.Write("Digite o senha: ");
            string senha = Console.ReadLine();

            bool entrada = Login_view.CadastroCliente(nome,email,fone,senha);

            return entrada;
        }

    }
}