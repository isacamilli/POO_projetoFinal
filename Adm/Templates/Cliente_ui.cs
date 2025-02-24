using Adm.View;
using Adm.Models;

namespace Adm.Templates
{
    public class Cliente_UI{
        public static int Menu_cliente(){
            Console.WriteLine("\n-------------------------------------");
            Console.WriteLine("\nTela de cliente");

            

            int numero = 1;

            while (numero != 0){
                Console.WriteLine("\n-------------------------------------");
                Console.WriteLine("\nEscolha uma das opções");
                Console.WriteLine("\n1 - Listar clientes");
                Console.WriteLine("2 - Mostrar cliente especifico");
                Console.WriteLine("3 - Excluir Cliente");
                Console.WriteLine("4 - Entrar em armario");
                Console.WriteLine("5 - Entrar em Tipo Roupa");
                Console.WriteLine("6 - Voltar");
                Console.WriteLine("0 - Sair do sistema");

                Console.Write("\nDigite aqui: ");

                if (int.TryParse(Console.ReadLine(), out numero))
                {
                    switch (numero)
                    { 
                        case 0:

                            return 0;
                            
                            break;

                        case 1:
                            
                            Console.WriteLine("\n");
                            listar_clientes();
                            break;

                        case 2:

                            Console.Write("\nDigite o nome do usuário que deseja escolher: ");

                            string nome = Console.ReadLine();
                            
                            int id_escolhido = listarId(nome);

                            if (id_escolhido != 0){
                                Console.Write("\nDeseja ver as roupas do cliente? ");
                                string escolha = Console.ReadLine(); 
                                if (escolha.ToLower() == "sim"){
                                    Console.WriteLine("\n");
                                    Roupa_UI.lista_roupas_id(id_escolhido);
                                }
                            }

                            break;

                        case 3:
                            excluir_cliente();

                            break;

                        case 4:
                            numero = Roupa_UI.menu_armario();
                            break;

                        case 6:
                            return 1;
                                        
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
            return 0;
        }

        public static void listar_clientes(){
            foreach (Cliente i in Cliente_view.listar_clientes()){
                Console.WriteLine(i);
            }
        }

        public static int listarId(string nome){

            foreach(Cliente i in Cliente_view.listar_clientes()){
                if (nome == i.getNome() ){
                    Console.WriteLine($"\n{i}");

                    return i.getId();
                }
            }
            return 0;

        }

        public static void excluir_cliente(){
            Console.Write("\nDigite o nome do usuário que deseja excluir: ");
            string nome = Console.ReadLine();

            int id_escolhido = listarId(nome);

            Cliente_view.excluir_cliente(id_escolhido);            
        }


    }
}