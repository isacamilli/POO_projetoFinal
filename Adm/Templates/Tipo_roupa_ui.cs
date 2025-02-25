using Adm.View;
using Adm.Models;

namespace Adm.Templates {

    public class TipoRoupa_UI {

        public static int menu_tipoR(){
            Console.WriteLine("\n-------------------------------------");
            Console.WriteLine("\nTela tipo de roupa");

            

            int numero = 1;

            while (numero != 0){
                Console.WriteLine("\n-------------------------------------");

                Console.WriteLine("\nEscolha uma das opções");

                Console.WriteLine("\n1 - Listar tipos de roupas");
                Console.WriteLine("2 - Adicionar tipo de roupa");
                Console.WriteLine("3 - Excluir tipo de roupa");
                Console.WriteLine("4 - Atualizar tipo de roupa");
                Console.WriteLine("5 - Filtrar roupa por tipo");
                Console.WriteLine("6 - Voltar");
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
                            listar_TipoR();
                            break;

                        case 2 :
                            inserir_TipoR();
                            break;

                        case 3 :
                            excluir_tipoR();
                            break;


                        case 4 :
                            
                            atualiza_tipoR();
                            break;

                        case 5 :

                            int num = listar_TipoR();

                            if (num>0){
                                Console.Write("\nDigite o nome do tipo que quer mostrar: ");
                                string nome = Console.ReadLine();

                                TipoRoupa_UI.listar_roupas_tipo(nome);
                            }
                            break;

                        case 6:
                            return 1;
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

            return 0;

        }

        public static int listar_TipoR(){
            Console.WriteLine("\n");
            int num = 0;
            foreach(Tipo_roupa i in TipoR_view.listar_tipo()){
                Console.WriteLine(i);
                num++;
            }
            if (num == 0) Console.WriteLine("Nenhum tipo cadastrado ainda");
            return num;

        } 
        public static void listar_roupas_tipo(string nome) {
            int id_escolhido = 0;
            foreach (Tipo_roupa i in TipoR_view.listar_tipo()){
                if (i.getNome().ToLower() == nome.ToLower()){
                    id_escolhido = i.getId();
                    break;
                }
            
            }

            int num = TipoR_view.lista_roupas_tipo(id_escolhido); 

            if (num != 0) Console.WriteLine($"\nQuantidade de roupas por tipo encontradas: {num}");
            else Console.WriteLine($"Nenhuma roupa por tipo: {nome}, cadastrada");

        }

        public static void inserir_TipoR(){
            Console.Write("\nDigite o nome do novo tipo: ");
            string nome = Console.ReadLine();

            Console.WriteLine("Digite uma breve descrição:");
            string descr = Console.ReadLine();

            TipoR_view.inserir_TipoR(nome,descr);

        }

        public static void excluir_tipoR(){
            Console.Write("\nDigite o nome do tipo que deseja excluir: ");
            string nome = Console.ReadLine();
            int id_escolhido = TipoR_view.listarId(nome);

            TipoR_view.excluir_tipo(id_escolhido);
        }

        public static void atualiza_tipoR(){
            Console.Write("\nDigite o nome do tipo que deseja atualizar: ");
            string nome = Console.ReadLine();
            
            int id_escolhido = TipoR_view.listarId(nome);

            if (id_escolhido == 0){
                Console.WriteLine("\nTipo de roupa não encontrado");
                return;
            }

            Console.Write("\nDigite o novo nome do tipo: ");
            string novo_nome = Console.ReadLine();
            
            Console.WriteLine("\nDigite a novo descrição do tipo: ");
            string nova_desc = Console.ReadLine();

            TipoR_view.att_TipoRoupa(id_escolhido,novo_nome,nova_desc);

        }

    }
}