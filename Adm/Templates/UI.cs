using Adm.View;

namespace Adm.Templates
{
    public class UI{
        public static void Main(){
            Login_view.CriarAdmin();
            bool coiso = false;
            Console.WriteLine("-------------------------------------");
            Console.WriteLine("\nBem vindo ao cloudwear!");
            Console.WriteLine("\n-------------------------------------");

            Login_UI.menu_cadastro();
            
        }
    }
}
