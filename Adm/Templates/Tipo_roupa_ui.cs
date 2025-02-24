using Adm.View;
using Adm.Models;

namespace Adm.Templates {

    public class TipoRoupa_UI {

        public static void listar_TipoR(){
            foreach(Tipo_roupa i in TipoR_view.listar_tipo()){
                Console.WriteLine(i);
            }
        } 
        public static void listar_roupas_tipo(string nome) {
            foreach (Tipo_roupa i in TipoR_view.listar_tipo()){
                if (i.getNome == nome){
                    id_escolhido = i.getId();
                    break
                }

                

            }
        }

    }
}