using Adm.View;
using Adm.Models;

namespace Adm.Templates{
    public class Roupa_UI {
        public static void lista_roupas_id(string nome){
            int id = 0;

            foreach (Cliente i in Cliente_view.listar_clientes()){
                if (i.getNome() == nome) {
                    id = i.getId();
                }
            }

            foreach(Roupa x in Roupa_view.listar_roupa_id(id)){
                Console.WriteLine(x);
            }
        }

    }
}