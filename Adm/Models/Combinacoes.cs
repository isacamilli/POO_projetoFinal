using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;

namespace Adm.Models
{
    public class Combinacoes : CRUD<Combinacao>
    {

        public override void Salvar()
        {
            if (!Directory.Exists("../../Data"))
            {
                Directory.CreateDirectory("../../Data");
            }

            try
            {
                using (StreamWriter arquivo = new StreamWriter("../../Data/combinacao.json"))
                {
                    var dados = new List<Dictionary<string, object>>();
                    foreach (var combinacao in objetos)
                    {
                        dados.Add(combinacao.ToDict());  
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
                using (StreamReader reader = new StreamReader("../../Data/combinacao.json"))
                {
                    string json = reader.ReadToEnd();  // Lê o conteúdo do arquivo JSON
                    var listaCombinacoes = JsonConvert.DeserializeObject<List<Dictionary<string, object>>>(json);

                    if (listaCombinacoes != null)
                    {
                        objetos.Clear();
                        foreach (var obj in listaCombinacoes)
                        {
                            // Cria o objeto combinacao a partir do dicionário
                            var combinacao = new Combinacao(
                                Convert.ToInt32(obj["id"]),
                                obj["clima"].ToString(),
                                Convert.ToInt32(obj["id_itens"])
                            );

                            objetos.Add(combinacao);  // Adiciona o combinacao à lista
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
