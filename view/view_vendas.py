from datetime import datetime
from controller.controller_vendas import ControllerVendas
from controller.controller_cliente import ControllerCliente
from controller.controller_funcionario import ControllerFuncionario
from controller.controller_produto import ControllerProduto


def menu_vendas():
    print(
        "----==funcionario==----\n"
        "1 - add venda\n"
        "2 - exibir vendas\n"
        "3 - editar venda\n"
        "4 - excluir venda\n"
        "5 - retornar ao menu principal\n"
        "6 - sair do programa\n"
        "----==============----\n"
    )

    op = input("Escolha um numero: ")

    if op == "1":
        print(ControllerProduto.exibe())
        id_produto = input("id do produto: ")
        quantidade_desejada = int(input("Digite a quantidade: "))
        print(ControllerCliente.exibe_clientes())
        id_cliente = input("id do cliente: ")
        print(ControllerFuncionario.exibir())
        id_vendedor = input("id do vendedor: ")
        data = input("enter para data atual ou digite a data dd/mm/aaaa: ")
      

        produto_existe = ControllerProduto.verifica_se_existe(id_produto, "id")
        cliente_existe = ControllerCliente.verifica_se_existe_cliente(id_cliente, "id")
        funcionario_existe = ControllerFuncionario.verifica_se_existe(id_vendedor, "id")

        # verifica se cliente, fornecedor e produto existem
        if produto_existe and cliente_existe and funcionario_existe:
            quantidade_disponivel = int(ControllerProduto.quant_disponivel(id_produto))
            
            estoque_maior_igual = ControllerProduto.verifica_estoque(
                quantidade_disponivel,
                quantidade_desejada,
            )

            # verifica se quantidade produto é maior/igual que quantidade desejada
            if estoque_maior_igual:
                print("ate aqui tudo certo")
