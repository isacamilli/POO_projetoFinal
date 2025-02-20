using System;
using System.Collections.Generic;

namespace Adm.Models
{
    public abstract class CRUD<T> where T : Inter
    {
         protected List<T> objetos = new List<T>();

        public void Inserir(T obj)
        {
            Abrir();
            int id = 0;
            foreach (T x in objetos)
            {
                if (x.getId() > id)
                {
                    id = x.getId();
                }
            }
            obj.setId(id + 1);
            objetos.Add(obj);
            Salvar();

            
        }

        public List<T> Listar()
        {
            Abrir();
            return objetos;
        }

        public T ListarId(int id)
        {
            Abrir();
            foreach (T x in objetos)
            {
                if (x.getId() == id)
                {
                    return x;
                }
            }
            return default(T);
        }

        public void Atualizar(T obj)
        {
            T x = ListarId(obj.getId());
            if (x != null)
            {
                objetos.Remove(x);
                objetos.Add(obj);
                Salvar();
            }
        }

        public void Excluir(T obj)
        {
            T x = ListarId(obj.getId());
            if (x != null)
            {
                objetos.Remove(x);
                Salvar();
            }
        }

        public abstract void Salvar();
        public abstract void Abrir();
    }
}
