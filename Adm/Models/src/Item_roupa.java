package src;

import java.util.List;

public class Item_roupa {
    private int id;
    private List<Integer> listaIdRoupas;

    public ItemRoupa(int id, List<Integer> listaIdRoupas) {
        setId(id);
        setLista(listaIdRoupas);
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
        this.listaIdRoupas = listaIdRoupas;
    }

    public int getId() {
        return this.id;
    }

    public List<Integer> getListaIdRoupas() {
        return this.listaIdRoupas;
    }

    public String toString() {
        return String.format("%d - %s", id, listaIdRoupas);
    }

    public Map<String, Object> toDict() {
        Map<String, Object> dict = new HashMap<>();
        dict.put("id", this.id);
        dict.put("listaIdRoupas", this.listaIdRoupas);
        return dict;
    }
}