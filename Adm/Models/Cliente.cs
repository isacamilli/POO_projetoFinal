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
            SetId(id);   // Usando os setters para garantir a validação
            SetNome(nome);
            SetEmail(email);
            SetFone(fone);
            SetSenha(senha);
            SetAdm(adm);
        }

        // Métodos setters com validação
        public void SetId(int id)
        {
            if (id < 0)
            {
                throw new ArgumentException("ID inválido");
            }
            this.id = id;
        }

        public void SetNome(string nome)
        {
            if (string.IsNullOrWhiteSpace(nome))
            {
                throw new ArgumentException("Nome não pode ser vazio");
            }
            this.nome = nome;
        }

        public void SetEmail(string email)
        {
            if (string.IsNullOrWhiteSpace(email))
            {
                throw new ArgumentException("Email inválido");
            }
            this.email = email;
        }

        public void SetFone(string fone)
        {
            if (string.IsNullOrWhiteSpace(fone))
            {
                throw new ArgumentException("Fone não pode ser vazio");
            }
            this.fone = fone;
        }

        public void SetSenha(string senha)
        {
            if (string.IsNullOrWhiteSpace(senha))
            {
                throw new ArgumentException("Senha não pode ser vazia");
            }
            this.senha = senha;
        }

        public void SetAdm(bool adm)
        {
            this.adm = adm;
        }

        // Métodos getters
        public int GetId() => id;
        public string GetNome() => nome;
        public string GetEmail() => email;
        public string GetFone() => fone;
        public string GetSenha() => senha;
        public bool IsAdm() => adm;

        // Método para converter cliente em dicionário
        public Dictionary<string, object> ToDict()
        {
            return new Dictionary<string, object>
            {
                { "id", id },
                { "nome", nome },
                { "email", email },
                { "fone", fone },
                { "senha", senha },
                { "adm", adm }
            };
        }

        // Método ToString
        public override string ToString()
        {
            return $"Cliente: id={id}, nome={nome}, email={email}, fone={fone}, senha={senha}, adm={adm}";
        }
    }
}
