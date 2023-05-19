from dao import *
from model import *
from prettytable import PrettyTable


class ControllerCliente:
    @classmethod
    def add(cls, nome, fone, cpf):
        resposta = ""
        if DaoCliente.add("Cliente", nome=nome, fone=fone, cpf=cpf):
            resposta = "Cliente adicionado com sucesso"
        else:
            resposta = "Infelizmente ocorreu um erro no cadastro"

        return resposta

    @classmethod
    def exibe_clientes(cls):
        print("====================================================")
        tabela = PrettyTable(["ID", "NOME", "FONE", "CPF"])
        dados = DaoCliente.retorna_dados("Cliente")
        [tabela.add_row(linha) for linha in dados]

        return tabela

    @classmethod
    def editar_cliente(cls, id, nome, fone, cpf):
        resposta = ""
        if nome != "":
            DaoCliente.edit("Cliente", id, nome=nome)
            resposta += "Nome atualizado\n"

        if fone != "":
            DaoCliente.edit("Cliente", id, fone=fone)
            resposta += "Fone atualizado\n"

        if cpf != "":
            DaoCliente.edit("Cliente", id, cpf=cpf)
            resposta += "CPF atualizado"

        if cpf == "" and fone == "" and nome == "":
            resposta = "Nada para atualizar"

        return resposta

    @classmethod
    def excluir_cliente(cls, id):
        DaoCliente.excluir(id, "id", "Cliente")

        return "Cliente excluido com sucesso"

    @classmethod
    def verifica_se_existe_cliente(cls, dado, campo):
        return DaoCliente.verifica_se_existe(dado, campo, "Cliente")


class ControllerFornecedor:
    @classmethod
    def exibe_fornecedores(cls):
        print("====================================================")
        tabela = PrettyTable(["ID", "NOME", "CNPJ", "FONE"])
        dados = DaoCliente.retorna_dados("Fornecedor")
        [tabela.add_row(linha) for linha in dados]

        return tabela

    @classmethod
    def add_fornecedor(cls, nome, cnpj, fone):
        resposta = ""
        if DaoFornecedor.add("Fornecedor", nome=nome, cnpj=cnpj, fone=fone):
            resposta = "Fornecedor adicionado com sucesso"
        else:
            resposta = "Infelizmente ocorreu um erro no cadastro"

        return resposta

    @classmethod
    def verifica_se_existe_fornecedor(cls, dado, campo):
        return DaoFornecedor.verifica_se_existe(dado, campo, "Fornecedor")

    @classmethod
    def editar_fornecedor(cls, id, nome, cnpj, fone):
        resposta = ""
        if nome != "":
            DaoFornecedor.edit("Fornecedor", id, nome=nome)
            resposta += "Nome atualizado\n"

        if fone != "":
            DaoFornecedor.edit("Fornecedor", id, fone=fone)
            resposta += "Fone atualizado\n"

        if cnpj != "":
            DaoFornecedor.edit("Fornecedor", id, cnpj=cnpj)
            resposta += "CNPJ atualizado"

        if cnpj == "" and fone == "" and nome == "":
            resposta = "Nada para atualizar"

        return resposta

    @classmethod
    def excluir(cls, id):
        DaoFornecedor.excluir(id, "id", "Fornecedor")

        return "Fornecedor excluido com sucesso"


class ControllerFuncionario:
    @classmethod
    def add(cls, nome: str, fone: str, cpf: str, salario: str):
        resposta = ""
        if DaoFuncionario.add(
            "Funcionario", nome=nome, fone=fone, cpf=cpf, salario=salario
        ):
            resposta = "Funcionario adicionado com sucesso"
        else:
            resposta = "Infelizmente ocorreu um erro no cadastro"

        return resposta

    @classmethod
    def exibir(cls):
        print("====================================================")
        tabela = PrettyTable(["ID", "NOME", "FONE", "CPF", "SALARIO"])
        dados = DaoCliente.retorna_dados("Funcionario")
        [tabela.add_row(linha) for linha in dados]

        return tabela

    @classmethod
    def verifica_se_existe(cls, dado, campo):
        return DaoFuncionario.verifica_se_existe(dado, campo, "Funcionario")

    @classmethod
    def edit(cls, id, nome, fone, cpf, salario):
        resposta = ""
        if nome != "":
            DaoFuncionario.edit("Funcionario", id, nome=nome)
            resposta += "Nome atualizado\n"

        if fone != "":
            DaoFuncionario.edit("Funcionario", id, fone=fone)
            resposta += "Fone atualizado\n"

        if cpf != "":
            DaoFuncionario.edit("Funcionario", id, cpf=cpf)
            resposta += "CPF atualizado"

        if salario != "":
            DaoFuncionario.edit("Funcionario", id, salario=salario)
            resposta += "Salario atualizado"

        if salario == "" and fone == "" and nome == "" and cpf == "":
            resposta = "Nada para atualizar"

        return resposta

    @classmethod
    def excluir(cls, id):
        DaoFuncionario.excluir(id, "id", "Funcionario")

        return "Funcionario excluido."


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


if __name__ == "__main__":
    print(ControllerCliente.exibe_clientes())
