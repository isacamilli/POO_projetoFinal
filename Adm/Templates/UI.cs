using Adm.View;

namespace Adm.Templates
{
    public class UI{
        public static void Main(){
            Login_view.CriarAdmin();
            Console.WriteLine("-------------------------------------");
            Console.WriteLine("\nBem vindo ao cloudwear!");

            Login_UI.menu_cadastro();

            Console.WriteLine("\nSaindo do sistema....");

        }
    }
}
