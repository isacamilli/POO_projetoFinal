import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

public class Itens_roupas extends CRUD<Item_roupa> {

    @Override
    public void salvar() {
        try {
            FileWriter writer = new FileWriter("Data/item_roupa.json");
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
            FileReader reader = new FileReader("Data/item_roupa.json");
            Type listType = new TypeToken<List<Item_roupa>>(){}.getType();
            // Lê o arquivo JSON e desserializa para a lista de objetos
            List<Item_roupa> listaroupas_comb = new Gson().fromJson(reader, listType);
            if (listaroupas_comb != null) {
                objetos = listaroupas_comb; // Se o arquivo contiver dados, atualiza a lista objetos
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