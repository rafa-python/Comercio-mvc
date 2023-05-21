from prettytable import PrettyTable
from dao import DaoCliente


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

    @classmethod
    def retorna_dado(cls, id):
        return DaoCliente.retorna_dado(id, "Cliente")[0][1]