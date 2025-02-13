package src;


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
        try (FileWriter writer = new FileWriter("data/roupa.json")) {
            Gson gson = new Gson();
            gson.toJson(objetos, writer);
           
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void abrir() {
        objetos.clear();
        try (FileReader reader = new FileReader("data/roupa.json")) {
            Type listType = new TypeToken<List<Roupa>>() {}.getType();
            objetos = new Gson().fromJson(reader, listType);
            if (objetos == null) {
                objetos = new ArrayList<>(); // Inicializa a lista se o arquivo estiver vazio
            }
            
        } catch (FileNotFoundException e) {
            objetos = new ArrayList<>(); // Se o arquivo não existir, cria uma lista vazia
           
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}