using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;

namespace Adm.Models
{
    public class Clientes : CRUD<Cliente> {

        private static List<Cliente> Objetos = new List<Cliente>();

        public static void Salvar()
        {
            // Verificar se o diretório 'Data' existe, se não, criar
            if (!Directory.Exists("Data"))
            {
                Directory.CreateDirectory("Data");
            }

            // Escrever os dados no arquivo "cliente.json"
            using (StreamWriter arquivo = new StreamWriter("Data/cliente.json"))
            {
                var dados = new List<Dictionary<string, object>>();
                foreach (var cliente in Objetos)
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
        public override void Abrir()
        {
            // Inicializa a lista de objetos para evitar NullReferenceException
            if (Objetos == null)
            {
                Objetos = new List<Cliente>();  // Se Objetos for null, inicializa com lista vazia
            }

            try
            {
                // Lê o arquivo JSON
                using (StreamReader reader = new StreamReader("Data/cliente.json"))
                {
                    string json = reader.ReadToEnd();  // Lê todo o conteúdo do arquivo JSON
                    // Desserializa o JSON para a lista de objetos
                    List<Cliente> listaClientes = JsonConvert.DeserializeObject<List<Cliente>>(json);
                    if (listaClientes != null)
                    {
                        Objetos = listaClientes; // Se o arquivo contiver dados, atualiza a lista Objetos
                    }
                }
            }
            catch (FileNotFoundException)
            {
                // Arquivo não encontrado, não há dados para carregar
                Objetos = new List<Cliente>(); // Inicializa a lista vazia
            }
            catch (IOException e)
            {
                Console.WriteLine(e.Message);
            }
        }
    }
}
