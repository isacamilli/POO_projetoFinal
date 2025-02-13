import java.util.List;
import java.util.HashMap;
import java.util.Map;


public class Item_roupa implements Inter {
    private int id;
    private List<Integer> lista_id_roupas;

    public Item_roupa(int id, List<Integer> lista_id_roupas) {
        setId(id);
        setLista(lista_id_roupas);
    }

    public void setId(int id) {
        if (id < 0) {
            throw new IllegalArgumentException("ID item roupas inválido");
        }
        this.id = id;
    }

    public void setLista(List<Integer> listaIdRoupas) {
        if (listaIdRoupas == null || listaIdRoupas.isEmpty()) {
            throw new IllegalArgumentException("Lista itens roupas não pode estar vazia");
        }
        else{
            this.lista_id_roupas = listaIdRoupas;
        }
    }

    public int getId() {
        return this.id;
    }

    public List<Integer> getListaIdRoupas() {
        return this.lista_id_roupas;
    }

    public String toString() {
        return String.format("%d - %s", this.id, this.lista_id_roupas);
    }

    public Map<String, Object> toDict() {
        Map<String, Object> dict = new HashMap<>();
        dict.put("id", this.id);
        dict.put("lista_id_oupas", this.lista_id_roupas);
        return dict;
    }
}