using System;
using Adm.Models;  // Usando o namespace correto

namespace Adm.View
{
    public static Void CriarAdmin(){
        bool criado = false;
        foreach (Cliente i in Clientes.Listar()){
            if (i.nome == "admin"){
                criado = true
            }
            if (!criado){
                Cliente adm = new Cliente("admin","admin", 1234, 1234)
                Clientes.Inserir(adm)
            }
        }
    }
}
