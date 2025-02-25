using Adm.Models;

namespace Adm.View{

    public class TipoR_view {

        private static Tipos_roupas tipos = new Tipos_roupas();

        public static void inserir_TipoR(string nome, string descr){

            foreach (Tipo_roupa tr in tipos.Listar()){
                if (tr.getNome().ToLower() == nome.ToLower()){
                    Console.WriteLine("Nome de tipo já existente");
                    return;
                }
            }

            Tipo_roupa tipo = new Tipo_roupa(0,nome,descr);
            tipos.Inserir(tipo);
            Console.WriteLine("\nTipo inserido com sucesso");
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

        public static int lista_roupas_tipo(int id){

            int num = 0;
             
            foreach (Roupa i in Roupa_view.listar_roupas()){
                if (i.get_idTipo() == id){
                    Console.WriteLine(i);
                    num++;
                }
            }
            
            return num;
        }

        public static int listarId(string nome){
            int id_escolhido = 0;
            foreach(Tipo_roupa tr in listar_tipo()){
                if (nome == tr.getNome()){
                    return tr.getId();
                }
            }
            return id_escolhido;
        }

        public static void att_TipoRoupa(int id,string nome,string desc){
            Tipo_roupa t = new Tipo_roupa(id,nome,desc);
            tipos.Atualizar(t);
        }

    }
}