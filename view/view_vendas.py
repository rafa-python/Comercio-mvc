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
        "3 - vendas por data\n"
        "4 - cliente que mais comprou\n"
        "5 - vendedor que mais vendeu\n"
        "6 - retornar ao menu principal\n"
        "7 - sair do programa\n"
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

            nome_vendedor = ControllerFuncionario.retorna_dado(id_vendedor)
            nome_cliente = ControllerCliente.retorna_dado(id_cliente)
            nome_produto = ControllerProduto.retorna_nome(id_produto)
            preco_produto = float(ControllerProduto.retorna_preco(id_produto))
            preco_total = quantidade_desejada * preco_produto

            # verifica se quantidade produto é maior/igual que quantidade desejada
            if estoque_maior_igual:
                # ajustando a data
                if data == "":
                    data = datetime.now().strftime("%d/%m/%Y")

                    ControllerProduto.atualiza_estoque(id_produto, quantidade_disponivel, quantidade_desejada)
                    print(ControllerVendas.add(
                        nome_produto,
                        preco_total,
                        quantidade_desejada,
                        nome_cliente,
                        nome_vendedor,
                        id_cliente,
                        id_vendedor,
                        data,
                    ))

                else:
                    ControllerProduto.atualiza_estoque(id_produto, quantidade_disponivel, quantidade_desejada)
                    print(ControllerVendas.add(
                        nome_produto,
                        preco_total,
                        quantidade_desejada,
                        nome_cliente,
                        nome_vendedor,
                        id_cliente,
                        id_vendedor,
                        data,
                    ))
            
            else:
                print("Saldo insuficiente.")

        else:
            print(
                "Infelizmente cliente/produto/fornecedor podem nao ter cadastro no nosso sistema."
            )
    
    elif op == "2":
        # exibir vendas
        print(ControllerVendas.exibe())
    
    elif op == "3":
        resultados = ControllerVendas.vendas_por_data()
        
        for data, total_vendas in resultados:
            print("=================================")
            print("Data:", data)
            print("Total de Vendas:", total_vendas)
            print() 

    elif op == "4":
        # cliente que mais comprou
        resultado = ControllerVendas.vendas_por_cliente()
        # Verifique se há resultados
        if resultado:
            cliente, total_vendas = resultado
            print("Cliente que mais comprou:", cliente)
            print("Total de Vendas:", total_vendas)
        else:
            print("Não foram encontradas vendas")
    
    elif op == "5":
        # vendedor mais aloprado
        resultado = ControllerVendas.vendas_por_vendedor()
        # Verifique se há resultados
        if resultado:
            vendedor, total_vendas = resultado
            print("Vendedor mais aloprado:", vendedor)
            print("Total de Vendas:", total_vendas)
        else:
            print("Não foram encontradas vendas")