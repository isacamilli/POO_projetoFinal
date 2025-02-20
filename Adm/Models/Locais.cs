using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;

namespace Adm.Models
{
    public class Locais : CRUD<Local>
    {

        public override void Salvar()
        {
            if (!Directory.Exists("../../Data"))
            {
                Directory.CreateDirectory("../../Data");
            }

            try
            {
                using (StreamWriter arquivo = new StreamWriter("../../Data/local.json"))
                {
                    var dados = new List<Dictionary<string, object>>();
                    foreach (var local in objetos)
                    {
                        dados.Add(local.ToDict());  
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
                using (StreamReader reader = new StreamReader("../../Data/local.json"))
                {
                    string json = reader.ReadToEnd();  // Lê o conteúdo do arquivo JSON
                    var listaLocais = JsonConvert.DeserializeObject<List<Dictionary<string, object>>>(json);

                    if (listaLocais != null)
                    {
                        objetos.Clear();
                        foreach (var obj in listaLocais)
                        {
                            // Cria o objeto local a partir do dicionário
                            var local = new Local(
                                Convert.ToInt32(obj["id"]),
                                obj["local"].ToString()
                            );

                            objetos.Add(local);  // Adiciona o local à lista
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
