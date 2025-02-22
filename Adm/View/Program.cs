using Adm.Models;

namespace Adm.View
{
    public class Program
    {
        public static void Main()
        {
            // Seu código aqui, por exemplo:
            Login_view.CriarAdmin();

            Cliente cliente = new Cliente(1,"isa","admin", "1234", "1234",false);

            Clientes clientes = new Clientes();

            clientes.Inserir(cliente);

            Login_view.confEntrada("isa","1234");

            Login_view.confEntrada("oi","sdjad");
        }
    }
}
