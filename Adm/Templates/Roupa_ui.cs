using Adm.View;
using Adm.Models;

namespace Adm.Templates{
    public class Roupa_UI {

        public static int menu_armario(){
            Console.WriteLine("\n-------------------------------------");
            Console.WriteLine("\nTela de armario");

            

            int numero = 1;

            while (numero != 0){
                Console.WriteLine("\n-------------------------------------");

                Console.WriteLine("\nEscolha uma das opções");

                Console.WriteLine("\n1 - Listar roupas");
                Console.WriteLine("2 - Filtrar roupa por usuário");
                Console.WriteLine("3 - Filtrar roupa por tipo");
                Console.WriteLine("4 - Voltar");
                Console.WriteLine("0 - Sair do sistema");


                Console.Write("\nDigite aqui: ");

                if (int.TryParse(Console.ReadLine(), out numero))
                {
                    switch (numero)
                    { 
                        case 0 :
                            return 0;
                            break;

                        case 1 :
                            Console.WriteLine("\n");
                            listar_roupas();
                            break;

                        case 2 :

                            Console.Write("\nDigite o nome do usuário que deseja escolher: ");

                            string nome = Console.ReadLine();
                            
                            int id_escolhido = Cliente_UI.listarId(nome);

                            if (id_escolhido != 0){
                                Console.WriteLine("\n");
                                Roupa_UI.lista_roupas_id(id_escolhido);
                            }

                            break;

                        case 3:
                            
                            int num = TipoRoupa_UI.listar_TipoR();

                            if (num>0){
                                Console.Write("\nDigite o nome do tipo que quer mostrar: ");
                                nome = Console.ReadLine();

                                TipoRoupa_UI.listar_roupas_tipo(nome);
                            }

                            break;

                        case 4:
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

        public static void listar_roupas(){
            int num = 0;
            foreach (Roupa i in Roupa_view.listar_roupas()){
                Console.WriteLine(i);
                num++;
            }
            if (num == 0) Console.WriteLine("Nenhuma roupa cadastrada no sistema");
        }

        public static void lista_roupas_id(int id){

            int num = 0;
            
            foreach(Roupa x in Roupa_view.listar_roupa_id(id)){
                Console.WriteLine(x);
                num++;
            }

            if (num>0){
                Console.WriteLine($"\nNúmero de roupas encontradas: {num}");
            }
            else{
                Console.WriteLine("Armário vazio");
            }
        }


    }
}