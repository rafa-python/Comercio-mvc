from controller.controller_produto import ControllerProduto
from controller.controller_fornecedor import ControllerFornecedor


def menu_produto():
    print(
        "----==funcionario==----\n"
        "1 - add produto\n"
        "2 - exibir produtos\n"
        "3 - editar produto\n"
        "4 - excluir produto\n"
        "5 - retornar ao menu principal\n"
        "6 - sair do programa\n"
        "----==============----\n"
    )

    op = input("Escolha um numero: ")

    if op == "1":
        # add produto
        nome = input("nome: ")
        if ControllerProduto.verifica_se_existe(nome, "nome"):
            print("Produto ja cadastrado.")

        else:
            preco = float(input("preco: "))
            categoria = input("categoria: ")
            quantidade = int(input("quantidade: "))
            print(ControllerFornecedor.exibe_fornecedores())
            id_fornecedor = input("informe o id do fornecedor: ")

            if ControllerFornecedor.verifica_se_existe_fornecedor(id_fornecedor, "id"):
                nome_fornecedor = ControllerProduto.nome_fornecedor(id_fornecedor)
                print(
                    ControllerProduto.add(
                        nome,
                        preco,
                        categoria,
                        quantidade,
                        nome_fornecedor,
                        id_fornecedor,
                    )
                )

            else:
                print("Fornecedor nao encontrado.")

    elif op == "2":
        print(ControllerProduto.exibe())

    elif op == "3":
        # editar produto
        print(ControllerProduto.exibe())
        id = input("id: ")

        if ControllerProduto.verifica_se_existe(id, "id"):
            nome = input("nome ou enter: ")
            preco = input("preco ou enter: ")
            categoria = input("categoria ou enter: ")
            quantidade = input("quantidade ou enter: ")
            print(ControllerFornecedor.exibe_fornecedores())
            id_fornecedor = input("informe o id do fornecedor ou enter: ")

            if ControllerFornecedor.verifica_se_existe_fornecedor(id_fornecedor, "id"):
                nome_fornecedor = ControllerProduto.nome_fornecedor(id_fornecedor)
                print(
                    ControllerProduto.edit(
                        id,
                        nome,
                        preco,
                        categoria,
                        quantidade,
                        nome_fornecedor,
                        id_fornecedor,
                    )
                )

            elif id_fornecedor == "":
                nome_fornecedor = ""
                print(
                    ControllerProduto.edit(
                        id,
                        nome,
                        preco,
                        categoria,
                        quantidade,
                        nome_fornecedor,
                        id_fornecedor,
                    )
                )

            else:
                print("Fornecedor nao encontrado.")

        else:
            print("Produto nao encontrado.")

    elif op == "4":
        # excluir produto
        print(ControllerProduto.exibe())
        id = input("id: ")
        if ControllerProduto.verifica_se_existe(id, "id"):
            print(ControllerProduto.excluir(id))
        else:
            print("Produto nao encontrado na base de dados.")

    elif op == "5":
        from view import menu_geral

        menu_geral()

    elif op == "6":
        exit()

    else:
        print("Valor invalido, retornando ao menu funcionarios")
        menu_produto()
