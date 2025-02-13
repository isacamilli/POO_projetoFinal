package src;

import java.util.ArrayList;
import java.util.List;

public abstract class CRUD<T> {
    protected List<T> objetos = new ArrayList<>();

    public void inserir(T obj) {
        abrir();
        int id = 0;
        for (T x : objetos) {
            if (x.getId() > id) {
                id = x.getId();
            }
        }
        obj.setId(id + 1);
        objetos.add(obj);
        salvar();
    }

    public List<T> listar() {
        abrir();
        return objetos;
    }

    public T listarId(int id) {
        abrir();
        for (T x : objetos) {
            if (x.getId() == id) {
                return x;
            }
        }
        return null;
    }

    public void atualizar(T obj) {
        T x = listarId(obj.getId());
        if (x != null) {
            objetos.remove(x);
            objetos.add(obj);
            salvar();
        }
    }

    public void excluir(T obj) {
        T x = listarId(obj.getId());
        if (x != null) {
            objetos.remove(x);
            salvar();
        }
    }

    public abstract void salvar();
    public abstract void abrir();
}