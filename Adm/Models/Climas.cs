// using Newtonsoft.Json;
// using System;
// using System.Collections.Generic;
// using System.IO;

// namespace Adm.Models
// {
//     public class Climas : CRUD<PeriodoClima>
//     {
//         public override void Salvar()
//         {
//             if (!Directory.Exists("../../Data"))
//             {
//                 Directory.CreateDirectory("../../Data");
//             }

//             try
//             {
//                 using (StreamWriter arquivo = new StreamWriter("../../Data/roupa.json")){
//                 List<Dictionary<string, object>> dados = new List<Dictionary<string, object>>();

//                 foreach (var clima in objetos)
//                 {
//                     dados.Add(new Dictionary<string, object>
//                     {
//                         { "id", clima.getId() },
//                         { "cidade", clima.getCidade() },
//                         { "pais", clima.getPais() },
//                         { "data", clima.getData().ToString("dd/MM/yyyy HH:mm") },
//                         { "clima", clima.getClima() },
//                         { "periodo", clima.getPeriodo() },
//                         { "temperatura", clima.getTemperatura() },
//                         { "sensacao_termica", clima.getSensacaoTermica() }
//                     });
//                 }

//                 // Serializa os dados para JSON e escreve no arquivo
//                 File.WriteAllText("../../Data/clima.json", JsonConvert.SerializeObject(dados, Formatting.Indented));
//             }
//             }
//             catch (IOException e)
//             {
//                 Console.WriteLine(e.Message);
//             }
//         }

//         public override void Abrir()
//         {
//             try
//             {
//                 using (StreamReader reader = new StreamReader("../../Data/clima.json"))
//                 {
//                     string json = reader.ReadToEnd();
//                     var listaClimas = JsonConvert.DeserializeObject<List<Dictionary<string, object>>>(json);

//                     if (listaClimas != null)
//                     {
//                         objetos.Clear();
//                         foreach (var obj in listaClimas)
//                         {
//                             var clima = new PeriodoClima(
//                                 Convert.ToInt32(obj["id"]),
//                                 obj["cidade"].ToString(),
//                                 obj["clima"].ToString(),
//                                 obj["pais"].ToString(),
//                                 Convert.ToSingle(obj["temperatura"]),
//                                 Convert.ToSingle(obj["sensacao_termica"]),
//                                 DateTime.Parse(obj["data"].ToString()),
//                                 obj["periodo"].ToString()
//                             );


//                             objetos.Add(clima);
//                         }
//                     }
//                 }
//             }
//             catch (FileNotFoundException)
//             {
//                 // Arquivo ainda não existe, não faz nada
//             }
//             catch (IOException e)
//             {
//                 Console.WriteLine(e.Message);
//             }
//         }
//     }
// }
