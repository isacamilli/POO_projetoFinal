using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;

namespace Adm.Models
{
    public class Tipos_roupas : CRUD<Tipo_roupa>
    {

        public override void Salvar()
        {
            if (!Directory.Exists("../../Data"))
            {
                Directory.CreateDirectory("../../Data");
            }

            try
            {
                using (StreamWriter arquivo = new StreamWriter("../../Data/tipo_roupa.json"))
                {
                    var dados = new List<Dictionary<string, object>>();
                    foreach (var tipo_roupa in objetos)
                    {
                        dados.Add(tipo_roupa.ToDict());  
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
                using (StreamReader reader = new StreamReader("../../Data/tipo_roupa.json"))
                {
                    string json = reader.ReadToEnd();  // Lê o conteúdo do arquivo JSON
                    var listaTipos_roupas = JsonConvert.DeserializeObject<List<Dictionary<string, object>>>(json);

                    if (listaTipos_roupas != null)
                    {
                        objetos.Clear();
                        foreach (var obj in listaTipos_roupas)
                        {
                            // Cria o objeto Tipo_roupa a partir do dicionário
                            var tipo_roupa = new Tipo_roupa(
                                Convert.ToInt32(obj["id"]),
                                obj["nome"].ToString(),
                                obj["descricao"].ToString()
                            );

                            objetos.Add(tipo_roupa);  // Adiciona o Tipo_roupa à lista
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
