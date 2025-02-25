using System;
using Adm.Models;  // Usando o namespace correto

namespace Adm.View
{
    public class Login_view{
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
                if (i.getNome().ToLower() == nome.ToLower()){
                    if (i.getSenha() == senha){
                        if (i.isAdm() == true){
                            admin = true;
                            Console.WriteLine("\nAcesso permitido!");
                            Console.WriteLine("Bem vindo Admin");
                            return admin;
                        }
                    } else {
                        Console.WriteLine("\nSenha incorreta");
                        return admin;
                    }

                    Console.WriteLine("\nProibido acesso de cliente");
                    return admin;
                }
            }
            Console.WriteLine("\nUsuário não encontrado");
            return admin;
        }

        public static bool CadastroCliente(string nome, string email,string fone,string senha){


            try{
                
                Cliente_view.inserir_cliente(nome,email,fone,senha);
                return true;
            }
            catch(IOException e){
                Console.WriteLine(e.Message);
                return false;
            }
        }
        
    }
}
