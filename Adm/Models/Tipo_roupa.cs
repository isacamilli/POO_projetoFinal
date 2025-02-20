using System;
using System.Collections.Generic;
using System.Linq;

namespace Adm.Models
{
    public class Tipo_roupa : Inter
    {
        // Atributos privados
        private int id;
        private string nome;
        private string descricao;

        public Tipo_roupa(int id,string nome, string descricao)
        {
            setId(id);
            setNome(nome);
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

        public void setNome(string nome)
        {
            if (string.IsNullOrWhiteSpace(nome))
            {
                throw new ArgumentException("nome não pode ser vazio");
            }
            this.nome = nome;
        }
        public void setDescricao(string descricao)
        {
            if (string.IsNullOrWhiteSpace(descricao))
            {
                throw new ArgumentException("descricao não pode ser vazio");
            }
            this.descricao = descricao;
        }


     
        // Métodos getters
        public int getId() => this.id;
        public string getNome() => this.nome;
        public string getDescricao() => this.descricao;

        
        public Dictionary<string, object> ToDict()
        {
            return new Dictionary<string, object>
            {
                { "id", this.id },
                { "nome", this.nome},
                {"descricao",this.descricao}
               };
            }

        // Método ToString
        public override string ToString()
        {
            return $"Cliente: id={this.id}, nome={this.nome}, descrição={this.descricao}";
        }
    }
}
        
