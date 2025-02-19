using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;

namespace Adm.Models
{
    public class Itens_roupas : CRUD<Item_roupa>
    {

        public override void Salvar()
        {
            if (!Directory.Exists("../../Data"))
            {
                Directory.CreateDirectory("../../Data");
            }

            try
            {
                using (StreamWriter arquivo = new StreamWriter("../../Data/item_roupa.json"))
                {
                    var dados = new List<Dictionary<string, object>>();
                    foreach (var item_roupa in objetos)
                    {
                        dados.Add(item_roupa.ToDict());  
                    }

                    string json = JsonConvert.SerializeObject(dados);
                    arquivo.Write(json);
                }
            }
            catch (IOException e)
            {
                Console.WriteLine(e.Message);
            }
        }

        public override void Abrir()
        {
            try
            {
                using (StreamReader reader = new StreamReader("../../Data/item_roupa.json"))
                {
                    string json = reader.ReadToEnd();  // Lê o conteúdo do arquivo JSON
                    var listaItens_roupas = JsonConvert.DeserializeObject<List<Dictionary<string, object>>>(json);

                    if (listaItens_roupas != null)
                    {
                        objetos.Clear();
                        foreach (var obj in listaItens_roupas)
                        {
                            // Cria o objeto item_roupa a partir do dicionário
                            var item_roupa = new Item_roupa(
                                Convert.ToInt32(obj["id"]),
                                JsonConvert.DeserializeObject<List<int>>(obj["lista_id_roupas"].ToString())
                            );

                            objetos.Add(item_roupa);  // Adiciona o item_roupa à lista
                        }
                    }
                }
            }
            catch (FileNotFoundException)
            {
                // Não faz nada se o arquivo não for encontrado
            }
            catch (IOException e)
            {
        
            }
        }
    }
}
