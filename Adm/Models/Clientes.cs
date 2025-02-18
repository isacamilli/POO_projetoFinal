using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;

namespace Adm.Models
{
    public class Clientes : CRUD<Cliente> {


        public static void Salvar()
        {
            if (!Directory.Exists("Data"))
            {
                Directory.CreateDirectory("Data");
            }

            using (StreamWriter arquivo = new StreamWriter("Data/cliente.json"))
            {
                var dados = new List<Dictionary<string, object>>();
                foreach (var cliente in objetos)
                {
                    dados.Add(cliente.ToDict());  // Convertendo o cliente para dicionário
                }

                // Serializar a lista de dicionários e gravar no arquivo JSON
                string json = JsonConvert.SerializeObject(dados);
                arquivo.Write(json);
            }
            catch (IOException e)
            {
                Console.WriteLine(e.Message);
            }
        }

        // Sobrescrevendo o método abrir
        public static void Abrir(){
            try {
                using (StreamReader reader = new StreamReader("Data/cliente.json")) {
                    string json = reader.ReadToEnd(); 
                    var listaClientes = JsonConvert.DeserializeObject<List<Dictionary<string, object>>>(json);

                    if (listaClientes != null)
                    {
                        foreach (var obj in listaClientes)
                        {
                            // Cria o objeto Cliente a partir do dicionário
                            var cliente = new Cliente(
                                Convert.ToInt32(obj["id"]),
                                obj["nome"].ToString(),
                                obj["email"].ToString(),
                                obj["fone"].ToString(),
                                obj["senha"].ToString(),
                                Convert.ToBoolean(obj["adm"])
                            );

                            objetos.Add(cliente);  // Adiciona o cliente à lista
                        }
                    }
                }
            }
            catch (FileNotFoundException)
            {

                        }
            catch (IOException e)
            {
                Console.WriteLine("Erro de I/O: " + e.Message);
            }
        }
    }
}
