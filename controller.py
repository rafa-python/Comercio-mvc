from dao import *
from model import *

class ControllerCliente:
    @classmethod
    def add(cls, nome, fone, cpf):
        resposta = ""
        if DaoCliente.add("Cliente", nome=nome, fone=fone, cpf=cpf):
            resposta = "Cliente adicionado com sucesso"
        else:
            resposta = "Infelizmente ocorreu um erro no cadastro"
        
        return resposta

if __name__ == "__main__":
    nome = input("Nome: ")
    fone = input("fone: ")
    cpf = input("cpf: ")

    cliente = Cliente(nome, fone, cpf)

    print(ControllerCliente.add(cliente.nome, cliente.fone, cliente.cpf))