using Adm.Models;

namespace Adm.View {
    public class Roupa_view{
        private static Roupas roupas = new Roupas(); 

        public static List<Roupa> listar_roupas(){
            return roupas.Listar();
        }

        public static List<Roupa> listar_roupa_id(int id){

            List<Roupa> lista_roupas = new List<Roupa>();

            foreach (Roupa i in Roupa_view.listar_roupas()){
                if (i.get_idCliente() == id){
                    lista_roupas.Add(i);
                }
            }
            return lista_roupas;
        }

    }
}