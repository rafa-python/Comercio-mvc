from controller.controller_fornecedor import ControllerFornecedor


def menu_fornecedor():
    print(
        "----==Fornecedor==----\n"
        "1 - add fornecedor\n"
        "2 - exibir fornecedores\n"
        "3 - editar fornecedor\n"
        "4 - excluir fornecedor\n"
        "5 - retornar ao menu principal\n"
        "6 - sair do programa\n"
        "----==============----\n"
    )

    op = input("Escolha um numero: ")

    if op == "1":
        cnpj = input("cnpj: ")
        if ControllerFornecedor.verifica_se_existe_fornecedor(cnpj, "cnpj"):
            print("Fornecedor ja possui cadastro")
        else:
            nome = input("nome: ")
            fone = input("fone: ")
            print(ControllerFornecedor.add_fornecedor(nome, cnpj, fone))

    elif op == "2":
        print(ControllerFornecedor.exibe_fornecedores())

    elif op == "3":
        print(ControllerFornecedor.exibe_fornecedores())
        id = input("Informe o id: ")

        if ControllerFornecedor.verifica_se_existe_fornecedor(id, "id"):
            nome = input("nome ou enter: ")
            cnpj = input("cnpj ou enter: ")
            fone = input("fone ou enter: ")
            print("==================================")
            print(ControllerFornecedor.editar_fornecedor(id, nome, cnpj, fone))

        else:
            print("Fornecedor nao encontrado na base de dados")

    elif op == "4":
        # excluir fornecedor
        print(ControllerFornecedor.exibe_fornecedores())
        id = input("Informe o id: ")

        if ControllerFornecedor.verifica_se_existe_fornecedor(id, "id"):
            print(ControllerFornecedor.excluir(id))

    elif op == "5":
        from view import menu_geral

        menu_geral()

    elif op == "6":
        exit()

    else:
        print("Valor invalido, retornando ao menu fornecedor")
        menu_fornecedor()
