using System;
using System.Collections.Generic;

namespace Adm.Models
{
    public class Local : Inter
    {
        // Atributos privados
        private int id;
        private string cidade;

        public Local(int id, string cidade)
        {
            setId(id);
            setCidade(cidade);
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

        public void setCidade(string cidade)
        {
            if (string.IsNullOrWhiteSpace(cidade))
            {
                throw new ArgumentException("cidade não pode ser vazio");
            }
            this.cidade = cidade;
        }


     
        // Métodos getters
        public int getId() => this.id;
        public string getCidade() => this.cidade;

        
        public Dictionary<string, object> ToDict()
        {
            return new Dictionary<string, object>
            {
                { "id", this.id },
                { "cidade", this.cidade}
               };
            }

        // Método ToString
        public override string ToString()
        {
            return $"Cliente: id={this.id}, cidade={this.cidade}";
        }
    }
}
        
