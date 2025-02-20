using System;
using System.Collections.Generic;

namespace Adm.Models
{
    public class Combinacao : Inter
    {
        // Atributos privados
        private int id;
        private string clima;
        private int id_itens;

        public Combinacao(int id, string clima, int id_itens)
        {
            setId(id);
            setClima(clima);
            set_idItens(id_itens);
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

        public void setClima(string clima)
        {
            if (string.IsNullOrWhiteSpace(clima))
            {
                throw new ArgumentException("clima não pode ser vazio");
            }
            this.clima = clima;
        }

        public void set_idItens(int id_itens)
        {
            if (id_itens < 0)
            {
                throw new ArgumentException("ID itens inválido");
            }
            this.id_itens = id_itens;
        }

     
        // Métodos getters
        public int getId() => this.id;
        public string getClima() => this.clima;
        public int get_idItens() => this.id_itens;
        
        public Dictionary<string, object> ToDict()
        {
            return new Dictionary<string, object>
            {
                { "id", this.id },
                { "clima", this.clima},
                { "id_itens", this.id_itens }
               };
            }

        // Método ToString
        public override string ToString()
        {
            return $"Cliente: id={this.id}, clima={this.clima}, id_itens={this.id_itens}";
        }
    }
}
        
