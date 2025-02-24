using Adm.Models;

namespace Adm.View{

    public class TipoR_view {

        private static Tipos_roupas tipos = new Tipos_roupas();

        public static void inserir_TipoR(string nome, string descr){
            Tipo_roupa tipo = new Tipo_roupa(0,nome,descr);
            tipos.Inserir(tipo);
        }

        public static List<Tipo_roupa> listar_tipo() {

            return tipos.Listar();
        }

        public static void excluir_tipo(int id){
            Tipo_roupa tipo = tipos.ListarId(id);

            if (tipo != null){
                tipos.Excluir(tipo);
                Console.WriteLine("\nTipo de roupa excluido com sucesso.");
            }
            else Console.WriteLine("\nTipo de roupa não encontrado");
        }

        public static void lista_roupas_tipo(int id){
            foreach (Tipo_roupa i in listar_tipo()){
                if 
            }
        }

    }
}