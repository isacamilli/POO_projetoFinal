using Adm.Models;

namespace Adm.View{
    public class Cliente_view{

        private static Clientes clientes = new Clientes(); 

        public static void inserir_cliente(string nome, string email, string fone, string senha){
            Cliente c = new Cliente(0,nome,email,fone,senha,false);
            clientes.Inserir(c);
            Console.WriteLine("\nCliente inserido no sistema com sucesso");
        }

        public static void excluir_cliente(int id){
            Cliente c = clientes.ListarId(id);

            if (c != null){
                clientes.Excluir(c);
                Console.WriteLine("\nCliente excluido com sucesso");
            }

            else{
                Console.WriteLine("\nCliente não encontrado");
            }

        }

    }
}