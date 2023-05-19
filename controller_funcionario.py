from prettytable import PrettyTable
from dao import DaoFuncionario, DaoCliente

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
