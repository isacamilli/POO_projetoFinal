using Adm.View;

namespace Adm.Templates
{
    public class UI{
        public static void Main(){
            Login.CriarAdmin();
            bool coiso = false;

            while (!coiso) {
                Console.Write("Digite o nome ou email do usuário: ");
                string nome = Console.ReadLine();

                Console.Write("Digite a senha: ");
                string senha = Console.ReadLine();

                coiso = Login.confEntrada(nome,senha);
            }
        }
    }
}
