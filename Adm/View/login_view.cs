using System;
using Adm.Models;  // Usando o namespace correto

namespace Adm.View
{
    public class Login{
        public static void CriarAdmin(){

            Clientes clientes = new Clientes(); 
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

        public static bool confEntrada()
        
    }
}
