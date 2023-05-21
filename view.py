from controller.controller_cliente import ControllerCliente
from controller.controller_funcionario import ControllerFuncionario
from controller.controller_fornecedor import ControllerFornecedor
from controller.controller_produto import ControllerProduto
from controller.controller_vendas import DaoVenda
from view.view_cliente import menu_cliente
from view.view_fornecedores import menu_fornecedor
from view.view_funcionario import menu_funcionario
from view.view_produto import menu_produto
from view.view_vendas import menu_vendas


def menu_geral():
    print(
        "----==Menu==----\n"
        "1 - cliente\n"
        "2 - fornecedores\n"
        "3 - funcionario\n"
        "4 - produto\n"
        "5 - vendas\n"
        "6 - sair do programa\n"
        "----========----\n"
    )

    op = input("Escolha um numero: ")

    if op == "1":
        # cliente
        menu_cliente()

    elif op == "2":
        # fornecedores
        menu_fornecedor()

    elif op == "3":
        # funcionario
        menu_funcionario()

    elif op == "4":
        # produto
        menu_produto()

    elif op == "5":
        # vendas
        menu_vendas()

    elif op == "6":
        # sair
        quit()

    else:
        print("Valor invalido")
        menu_geral()


if __name__ == "__main__":
    menu_geral()
