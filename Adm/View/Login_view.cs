using System;
using Adm.Models;  // Usando o namespace correto

namespace Adm.View
{
    public class Login{
            private static Clientes clientes = new Clientes(); 
        public static void CriarAdmin(){

            bool criado = false;
            foreach (Cliente i in clientes.Listar()){
                if (i.getNome() == "admin"){
                    criado = true;
                    break;
                }
            }

            if (!criado){
                Cliente adm = new Cliente(1,"admin","admin", "1234", "1234",true);
                clientes.Inserir(adm);
            }
        }

        public static bool confEntrada(string nome, string senha){
            bool admin = false;
            foreach (Cliente i in clientes.Listar()){
                if (i.getNome() == nome && i.getSenha() == senha){
                    if (i.getNome() == "admin"){
                        admin = true;
                        return admin;
                    }

                    Console.WriteLine("Proibido acesso de cliente");
                    return admin;
                }
            }
            Console.WriteLine("Usuário não encontrado");
            return admin;
        }
        
    }
}
