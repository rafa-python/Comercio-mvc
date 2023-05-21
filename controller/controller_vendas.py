from dao import DaoVenda
from prettytable import PrettyTable


class ControllerVendas:
    @classmethod
    def exibe(cls):
        print("====================================================")
        tabela = PrettyTable(
            [
                "ID",
                "PRODUTO",
                "PRECO",
                "QUANTIDADE",
                "CLIENTE",
                "VENDEDOR",
                "ID_CLIENTE",
                "ID_FORNECEDOR",
                "DATA",
            ]
        )
        dados = DaoVenda.retorna_dados("Vendas")
        [tabela.add_row(linha) for linha in dados]

        return tabela

    @classmethod
    def add(
        cls,
        produto,
        preco,
        quantidade,
        cliente,
        vendedor,
        id_cliente,
        id_vendedor,
        data,
    ):
        resposta = ""
        if DaoVenda.add(
            "Vendas",
            produto=produto,
            preco=preco,
            quantidade=quantidade,
            cliente=cliente,
            vendedor=vendedor,
            id_cliente=id_cliente,
            id_vendedor=id_vendedor,
            data=data,
        ):
            resposta = "Venda realizada"

        else:
            resposta = "Infelizmente ocorreu um erro nessa venda"

        return resposta
    
    @classmethod
    def vendas_por_data(cls):
        cursor, conn = DaoVenda.conecta_banco(r"D:\Comercio\banco.db")
        
        # Execute a consulta SQL para buscar as vendas por data
        cursor.execute("SELECT data, SUM(preco) as total_vendas FROM vendas GROUP BY data ORDER BY total_vendas DESC LIMIT 5")

        # Recupere os resultados da consulta
        resultados = cursor.fetchall()

        conn.close()

        return resultados
    
    @classmethod
    def vendas_por_cliente(cls):
        cursor, conn = DaoVenda.conecta_banco(r"D:\Comercio\banco.db")
        cursor.execute("SELECT cliente, SUM(preco) as total_vendas FROM Vendas GROUP BY cliente ORDER BY total_vendas DESC LIMIT 1")
        resultado = cursor.fetchone()
        conn.close()
        return resultado
    
    @classmethod
    def vendas_por_vendedor(cls):
        cursor, conn = DaoVenda.conecta_banco(r"D:\Comercio\banco.db")
        cursor.execute("SELECT vendedor, SUM(preco) as total_vendas FROM vendas GROUP BY vendedor ORDER BY total_vendas DESC LIMIT 1")
        resultado = cursor.fetchone()
        conn.close()
        return resultado






if __name__ == "__main__":
    pass
