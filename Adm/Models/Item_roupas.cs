using System;
using System.Collections.Generic;
using System.Linq;

namespace Adm.Models
{
    public class Item_roupa : Inter
    {
        // Atributos privados
        private int id;
        private List<int> lista_id_roupas;

        public Item_roupa(int id, List<int> lista_id_roupas)
        {
            setId(id);
            setLista(lista_id_roupas);
        }

        // Métodos setters com validação
        public void setId(int id)
        {
            if (id < 0)
            {
                throw new ArgumentException("ID inválido");
            }
            this.id = id;
        }

        public void setLista(List<int> lista_id_roupas)
        {
            if (lista_id_roupas.Count == 0){
                throw new ArgumentException("A lista de roupas não pode ser vazia.");
            }
            this.lista_id_roupas = lista_id_roupas;
        }


     
        // Métodos getters
        public int getId() => this.id;
        public List<int> getLista() => this.lista_id_roupas;

        
        public Dictionary<string, object> ToDict()
        {
            return new Dictionary<string, object>
            {
                { "id", this.id },
                { "lista_id_roupas", this.lista_id_roupas}
               };
            }

        // Método ToString
        public override string ToString()
        {
            return $"Cliente: id={this.id}, lista_id_roupas={this.lista_id_roupas}";
        }
    }
}
        
