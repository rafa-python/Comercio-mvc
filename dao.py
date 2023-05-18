from model import *
import sqlite3


class DaoBase:
    def __init__(self, nome_tabela, campos, db_arq):
        self.nome_tabela, self.campos, self.db_arq = nome_tabela, campos, db_arq
        self.criar_tabela()

    def criar_tabela(self):
        query = f"CREATE TABLE IF NOT EXISTS {self.nome_tabela} ("
        for campo, tipo_campo in self.campos.items():
            query += f"{campo} {tipo_campo}, "
        query = query[:-2]  # remove a ultima virgula e espaço
        query += ")"
        with sqlite3.connect(self.db_arq) as conn:
            conn.execute(query)

    @classmethod
    def conecta_banco(cls, banco):
        conn = sqlite3.connect(banco)
        cursor = conn.cursor()
        
        return cursor, conn
    
    @classmethod
    def add(cls, nome_tabela, **kwargs):
        cursor, conn = DaoBase.conecta_banco(r"D:\Comercio\banco.db")
        configuracoes = ", ".join([chave for chave in kwargs.keys()])
        valores = [f"{valor}" for valor in kwargs.values()]
        var_auxiliar = (len(valores) * "?, ")[:-2]
        query = f"INSERT INTO {nome_tabela} ({configuracoes}) VALUES ({var_auxiliar})"
        cursor.execute(query, valores)
        conn.commit()
        conn.close()

        return True
    
    @classmethod
    def edit(cls, nome_tabela, id, **kwargs):
        cursor, conn = DaoBase.conecta_banco(r"D:\Comercio\banco.db")
        configuracoes = ", ".join([f"{key} = ?" for key in kwargs.keys()])
        query = f"UPDATE {nome_tabela} SET {configuracoes} WHERE id = ?"
        valores = [*kwargs.values(), id]
        cursor.execute(query, valores)
        conn.commit()
        conn.close()
        
        return True
    
    @classmethod
    def excluir(cls, valor_campo, campo, tabela):
        cursor, conn = DaoBase.conecta_banco(r"D:\Comercio\banco.db")
        cursor.execute(f"DELETE FROM {tabela} WHERE {campo} = ?", (valor_campo,))
        conn.commit()
        conn.close()
        
        return True
    
    @classmethod
    def verifica_se_existe(cls, dado, campo, tabela):
        cursor, conn = DaoBase.conecta_banco(r"D:\Comercio\banco.db")
        query = f"SELECT {campo} FROM {tabela} WHERE {campo} = ?"
        cursor.execute(query, (dado,))
        resposta = cursor.fetchone()
        conn.close()
        
        return resposta
    
    @classmethod
    def retorna_dados(cls, tabela):
        cursor, conn = DaoBase.conecta_banco(r"D:\Comercio\banco.db")
        dados = list(cursor.execute(f"SELECT * FROM {tabela};"))
        conn.close()
        return dados


class DaoCliente(DaoBase):
    def __init__(self):
        campos = {
            "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "nome": "TEXT",
            "fone": "TEXT",
            "cpf": "TEXT"
        }
        super().__init__("Cliente", campos, "banco.db")


class DaoFornecedor(DaoBase):
    def __init__(self):
        campos = {
            "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "nome": "TEXT",
            "cnpj": "TEXT",
            "fone": "TEXT"
        }
        super().__init__("Fornecedor", campos, "banco.db")



if __name__ == "__main__":
    a=DaoFornecedor()
