from dao import DaoProduto, DaoFornecedor
from prettytable import PrettyTable


class ControllerProduto:
    @classmethod
    def exibe(cls):
        print("====================================================")
        tabela = PrettyTable(
            [
                "ID",
                "NOME",
                "PRECO",
                "CATEGORIA",
                "QUANTIDADE",
                "FORNECEDOR",
                "ID FORNECEDOR",
            ]
        )
        dados = DaoProduto.retorna_dados("Produto")
        [tabela.add_row(linha) for linha in dados]

        return tabela

    @classmethod
    def verifica_se_existe(cls, dado, campo):
        return DaoProduto.verifica_se_existe(dado, campo, "Produto")
    
    @classmethod
    def nome_fornecedor(cls, id):
        return DaoFornecedor.retorna_dado(id, "Fornecedor")[0][1]

    @classmethod
    def add(cls, nome, preco, categoria, quantidade, fornecedor, id_fornecedor):
        resposta = ""
        if DaoProduto.add(
            "Produto",
            nome=nome,
            preco=preco,
            categoria=categoria,
            quantidade=quantidade,
            fornecedor=fornecedor,
            id_fornecedor=id_fornecedor,
        ):
            resposta = "Produto adicionado com sucesso"
        else:
            resposta = "Infelizmente ocorreu um erro no cadastro"

        return resposta
    
    @classmethod
    def edit(cls, id, nome, preco, categoria, quantidade, fornecedor, id_fornecedor):
        resposta = ""
        if nome != "":
            DaoProduto.edit("Produto", id, nome=nome)
            resposta += "Nome atualizado\n"

        if preco != "":
            DaoProduto.edit("Produto", id, preco=preco)
            resposta += "Preço atualizado\n"

        if categoria != "":
            DaoProduto.edit("Produto", id, categoria=categoria)
            resposta += "Categoria atualizado\n"

        if quantidade != "":
            DaoProduto.edit("Produto", id, quantidade=quantidade)
            resposta += "Quantidade atualizado\n"
        
        if fornecedor != "":
            DaoProduto.edit("Produto", id, fornecedor=fornecedor)
            resposta += "Fornecedor atualizado\n"
        
        if id_fornecedor != "":
            DaoProduto.edit("Produto", id, id_fornecedor=id_fornecedor)
            resposta += "Id fornecedor atualizado\n"

        if nome == "" and preco == "" and categoria == "" and quantidade == "" and fornecedor == "" and id_fornecedor == "":
            resposta = "Nada para atualizar"

        return resposta
    
    @classmethod
    def excluir(cls, id):
        DaoProduto.excluir(id, "id", "Produto")

        return "Produto excluido."