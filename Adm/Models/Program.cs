using System;
using Adm.Models;  // Certifique-se de que o namespace está correto

class Program
{
    static void Main(string[] args)
    {

        Roupas roupasManager = new Roupas();
        Combinacoes comb = new Combinacoes();
        Locais loc = new Locais();

        Roupa roupa = new Roupa(
            id: 1,
            nome_roupa: "Camiseta",
            cor: "Azul",
            id_tipo: 3,
            detalhes: "Tamanho M, 100% algodão",
            id_cliente: 123
        );

        Combinacao comb1 = new Combinacao(
            id: 1,
            clima: "23",
            id_itens:2
        );

        Local loc1 = new Local(
            id: 1,
            cidade: "23"
        );

        Console.WriteLine(roupa.ToString());
        Console.WriteLine(comb1.ToString());

        roupasManager.Inserir(roupa);
        comb.Inserir(comb1);
        loc.Inserir(loc1);
    }
}
