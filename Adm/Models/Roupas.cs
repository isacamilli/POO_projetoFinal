using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;

namespace Adm.Models
{
    public class Roupas : CRUD<Roupa>
    {

        public override void Salvar()
        {
            if (!Directory.Exists("../../Data"))
            {
                Directory.CreateDirectory("../../Data");
            }

            try
            {
                using (StreamWriter arquivo = new StreamWriter("../../Data/roupa.json"))
                {
                    var dados = new List<Dictionary<string, object>>();
                    foreach (var roupa in objetos)
                    {
                        dados.Add(roupa.ToDict());  
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
                using (StreamReader reader = new StreamReader("../../Data/roupa.json"))
                {
                    string json = reader.ReadToEnd();  // Lê o conteúdo do arquivo JSON
                    var listaRoupas = JsonConvert.DeserializeObject<List<Dictionary<string, object>>>(json);

                    if (listaRoupas != null)
                    {
                        objetos.Clear();
                        foreach (var obj in listaRoupas)
                        {
                            // Cria o objeto Roupa a partir do dicionário
                            var roupa = new Roupa(
                                Convert.ToInt32(obj["id"]),
                                obj["nome_roupa"].ToString(),
                                obj["cor"].ToString(),
                                Convert.ToInt32(obj["id_tipo"]),
                                obj["detalhes"].ToString(),
                                Convert.ToInt32(obj["id_cliente"])
                            );

                            objetos.Add(roupa);  // Adiciona o Roupa à lista
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
