using System;
using Adm.Models;  // Certifique-se de que o namespace está correto

class Program
{
    static void Main(string[] args)
    {

        Roupas roupasManager = new Roupas();

        Roupa roupa = new Roupa(
            id: 1,
            nome_roupa: "Camiseta",
            cor: "Azul",
            id_tipo: 3,
            detalhes: "Tamanho M, 100% algodão",
            id_cliente: 123
        );

        Console.WriteLine(roupa.ToString());

        roupasManager.Inserir(roupa);
        
    }
}
