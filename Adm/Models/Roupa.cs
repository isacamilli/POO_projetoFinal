using System;
using System.Collections.Generic;

namespace Adm.Models
{
    public class Roupa : Inter
    {
        // Atributos privados
        private int id;
        private string nome_roupa;
        private string cor;
        private int id_tipo;
        private string detalhes;
        private int id_cliente;

        // Construtor que apenas inicializa os campos, sem validação
        public Roupa(int id, string nome_roupa, string cor, int id_tipo, string detalhes, int id_cliente)
        {
            setId(id);
            set_nomeRoupa(nome_roupa);
            setCor(cor);
            set_idTipo(id_tipo);
            setDetalhes(detalhes);
            set_idCliente(id_cliente);
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

        public void set_nomeRoupa(string nome_roupa)
        {
            if (string.IsNullOrWhiteSpace(nome_roupa))
            {
                throw new ArgumentException("Nome roupa não pode ser vazio");
            }
            this.nome_roupa = nome_roupa;
        }

        public void setCor(string cor)
        {
            if (string.IsNullOrWhiteSpace(cor))
            {
                throw new ArgumentException("cor inválido");
            }
            this.cor = cor;
        }

        public void set_idTipo(int id_tipo)
        {
            if (id_tipo < 0)
            {
                throw new ArgumentException("ID tipo inválido");
            }
            this.id_tipo = id_tipo;
        }

        public void setDetalhes(string detalhes)
        {
            if (string.IsNullOrWhiteSpace(detalhes))
            {
                throw new ArgumentException("detalhes não pode ser vazia");
            }
            this.detalhes = detalhes;
        }

        public void set_idCliente(int id_cliente)
        {
            if (id_cliente < 0)
            {
                throw new ArgumentException("ID roupa inválido");
            }
            this.id_cliente = id_cliente;
        }

        // Métodos getters
        public int getId() => this.id;
        public string getNome() => this.nome_roupa;
        public string getcor() => this.cor;
        public int get_idTipo() => this.id_tipo;
        public string getdetalhes() => this.detalhes;
        public int get_idRoupa() => this.id_cliente;

        // Método para converter cliente em dicionário
        public Dictionary<string, object> ToDict()
        {
            return new Dictionary<string, object>
            {
                { "id", this.id },
                { "nome_roupa", this.nome_roupa},
                { "cor", this.cor },
                { "id_tipo", this.id_tipo },
                { "detalhes", this.detalhes },
                { "id_cliente", this.id_cliente }
            };
        }

        // Método ToString
        public override string ToString()
        {
            return $"Cliente: id={this.id}, nome_roupa={this.nome_roupa}, cor={this.cor}, id_tipo={this.id_tipo}, detalhes={this.detalhes}, id_cliente={this.id_cliente}";
        }
    }
}
