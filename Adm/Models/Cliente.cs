// Cliente.cs
using System;
using System.Collections.Generic;

namespace Adm.Models
{
    public class Cliente : Inter
    {
        private int id;
        private string nome;
        private string email;
        private string fone;
        private string senha;
        private bool adm;

        public Cliente(int id, string nome, string email, string fone, string senha, bool adm) {
            SetId(id);
            SetNome(nome);
            SetEmail(email);
            SetFone(fone);
            SetSenha(senha);
            SetAdm(adm);
        }

        public int GetId()
        {
            return id;
        }

        public void SetId(int id)
        {
            if (id < 0)
            {
                throw new ArgumentException("id inválido");
            }
            this.id = id;
        }

        public Dictionary<string, object> ToDict()
        {
            var dict = new Dictionary<string, object>
            {
                { "id", this.id },
                { "nome", this.nome },
                { "email", this.email },
                { "fone", this.fone },
                { "senha", this.senha },
                { "adm", this.adm }
            };
            return dict;
        }

        public override string ToString()
        {
            return $"Cliente: id={this.id}, nome={this.nome}, email={this.email}, fone={this.fone}, senha={this.senha}, adm={this.adm}";
        }

        // Métodos setters
        public void SetNome(string nome)
        {
            if (string.IsNullOrEmpty(nome))
            {
                throw new ArgumentException("nome não pode ser vazio");
            }
            this.nome = nome;
        }

        public void SetEmail(string email)
        {
            if (email == null || !(email is string))
            {
                throw new ArgumentException("Email inválido");
            }
            this.email = email;
        }

        public void SetFone(string fone)
        {
            if (string.IsNullOrEmpty(fone))
            {
                throw new ArgumentException("fone não pode ser vazio");
            }
            this.fone = fone;
        }

        public void SetSenha(string senha)
        {
            if (string.IsNullOrEmpty(senha))
            {
                throw new ArgumentException("senha não pode ser vazia");
            }
            this.senha = senha;
        }

        public void SetAdm(bool adm)
        {
            this.adm = adm;
        }

        // Métodos getters
        public string GetNome()
        {
            return nome;
        }

        public string GetEmail()
        {
            return email;
        }

        public string GetFone()
        {
            return fone;
        }

        public string GetSenha()
        {
            return senha;
        }

        public bool IsAdm()
        {
            return adm;
        }
    }
}
