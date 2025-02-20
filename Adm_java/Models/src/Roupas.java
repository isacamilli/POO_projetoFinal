package Adm_java.Models.src;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

public class Roupas extends CRUD<Roupa> {

    @Override
    public void salvar() {
        try {
            FileWriter writer = new FileWriter("Data/roupa.json");
            Gson gson = new Gson();
            gson.toJson(objetos, writer); // Serializa os objetos e escreve no arquivo
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void abrir() {
        // Inicializa a lista objetos para evitar NullPointerException
        if (objetos == null) {
            objetos = new ArrayList<>();  // Se objetos for null, inicializa como lista vazia
        }

        try {
            FileReader reader = new FileReader("Data/roupa.json");
            Type listType = new TypeToken<List<Roupa>>(){}.getType();
            // Lê o arquivo JSON e desserializa para a lista de objetos
            List<Roupa> listaRoupas = new Gson().fromJson(reader, listType);
            if (listaRoupas != null) {
                objetos = listaRoupas; // Se o arquivo contiver dados, atualiza a lista objetos
            }
            reader.close();
        } catch (FileNotFoundException e) {
            // Arquivo não encontrado, não há dados para carregar
            objetos = new ArrayList<>(); // Inicializa a lista vazia
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}