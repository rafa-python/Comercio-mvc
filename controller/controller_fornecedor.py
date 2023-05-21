from dao import DaoFornecedor
from prettytable import PrettyTable


class ControllerFornecedor:
    @classmethod
    def exibe_fornecedores(cls):
        print("====================================================")
        tabela = PrettyTable(["ID", "NOME", "CNPJ", "FONE"])
        dados = DaoFornecedor.retorna_dados("Fornecedor")
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
