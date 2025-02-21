using Adm.Models;

namespace Adm.View
{
    public class Program
    {
        public static void Main()
        {
            // Seu código aqui, por exemplo:
            Login.CriarAdmin();

            Cliente cliente = new Cliente(1,"isa","admin", "1234", "1234",true);

            Clientes clientes = new Clientes();

            clientes.Inserir(cliente);

            Login.confEntrada("isa","1234");

            Login.confEntrada("oi","sdjad");
        }
    }
}
