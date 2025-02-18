using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;

namespace Adm.Models
{
    public class Climas : CRUD<PeriodoClima>
    {
        public override void Salvar()
        {
            if (!Directory.Exists("../../Data"))
            {
                Directory.CreateDirectory("../../Data");
            }

            try
            {
                using (StreamWriter arquivo = new StreamWriter("../../Data/clima.json"))
                {
                    var dados = new List<Dictionary<string, object>>();
                    foreach (var clima in objetos)
                    {
                        dados.Add(new Dictionary<string, object>
                        {
                            { "id", clima.Id },
                            { "cidade", clima.Cidade },
                            { "pais", clima.Pais },
                            { "data", clima.Data.ToString("dd/MM/yyyy HH:mm") },
                            { "clima", clima.Clima },
                            { "periodo", clima.Periodo },
                            { "temperatura", clima.Temperatura },
                            { "sensacao_termica", clima.SensacaoTermica }
                        });
                    }

                    string json = JsonConvert.SerializeObject(dados, Formatting.Indented);
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
                using (StreamReader reader = new StreamReader("../../Data/clima.json"))
                {
                    string json = reader.ReadToEnd();
                    var listaClimas = JsonConvert.DeserializeObject<List<Dictionary<string, object>>>(json);

                    if (listaClimas != null)
                    {
                        objetos.Clear();
                        foreach (var obj in listaClimas)
                        {
                            var clima = new PeriodoClima(
                                Convert.ToInt32(obj["id"]),
                                obj["cidade"].ToString()
                            );

                            clima.Clima = obj["clima"].ToString();
                            clima.Pais = obj["pais"].ToString();
                            clima.Temperatura = Convert.ToSingle(obj["temperatura"]);
                            clima.SensacaoTermica = Convert.ToSingle(obj["sensacao_termica"]);
                            clima.Data = DateTime.Parse(obj["data"].ToString());
                            clima.Periodo = obj["periodo"].ToString();

                            objetos.Add(clima);
                        }
                    }
                }
            }
            catch (FileNotFoundException)
            {
                // Arquivo ainda não existe, não faz nada
            }
            catch (IOException e)
            {
                Console.WriteLine(e.Message);
            }
        }
    }
}
