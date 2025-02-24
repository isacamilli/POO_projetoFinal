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
            foreach (Roupa i in Roupa_view.listar_roupas()){
                Console.WriteLine(i);
            }
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