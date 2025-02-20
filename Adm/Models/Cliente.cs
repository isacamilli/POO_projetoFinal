using System;
using System.Collections.Generic;

namespace Adm.Models
{
    public class Cliente : Inter
    {
        // Atributos privados
        private int id;
        private string nome;
        private string email;
        private string fone;
        private string senha;
        private bool adm;

        // Construtor que apenas inicializa os campos, sem validação
        public Cliente(int id, string nome, string email, string fone, string senha, bool adm)
        {
         setId(id);   // Usando os setters para garantir a validação
         setNome(nome);
         setEmail(email);
         setFone(fone);
         setSenha(senha);
         setAdm(adm);
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
                throw new ArgumentException("Nome não pode ser vazio");
            }
            this.nome = nome;
        }

        public void setEmail(string email)
        {
            if (string.IsNullOrWhiteSpace(email))
            {
                throw new ArgumentException("Email inválido");
            }
            this.email = email;
        }

        public void setFone(string fone)
        {
            if (string.IsNullOrWhiteSpace(fone))
            {
                throw new ArgumentException("Fone não pode ser vazio");
            }
            this.fone = fone;
        }

        public void setSenha(string senha)
        {
            if (string.IsNullOrWhiteSpace(senha))
            {
                throw new ArgumentException("Senha não pode ser vazia");
            }
            this.senha = senha;
        }

        public void setAdm(bool adm)
        {
            this.adm = adm;
        }

        // Métodos getters
        public int getId() => this.id;
        public string getNome() => this.nome;
        public string getEmail() => this.email;
        public string getFone() => this.fone;
        public string getSenha() => this.senha;
        public bool isAdm() => this.adm;

        // Método para converter cliente em dicionário
        public Dictionary<string, object> ToDict()
        {
            return new Dictionary<string, object>
            {
                { "id", this.id },
                { "nome", this.nome },
                { "email", this.email },
                { "fone", this.fone },
                { "senha", this.senha },
                { "adm", this.adm }
            };
        }

        // Método ToString
        public override string ToString()
        {
            return $"Cliente: id={id}, nome={nome}, email={email}, fone={fone}, senha={senha}, adm={adm}";
        }
    }
}
