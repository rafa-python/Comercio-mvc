from controller.controller_cliente import ControllerCliente


def menu_cliente():
    print(
        "----==Cliente==----\n"
        "1 - add cliente\n"
        "2 - exibir clientes\n"
        "3 - editar cliente\n"
        "4 - excluir cliente\n"
        "5 - retornar ao menu principal\n"
        "6 - sair do programa\n"
        "----========----\n"
    )

    op = input("Escolha um numero: ")

    if op == "1":
        # add cliente
        cpf = input("cpf: ")
        if ControllerCliente.verifica_se_existe_cliente(cpf, "cpf"):
            print("Cliente ja possui cadastro")
        else:
            nome = input("nome: ")
            fone = input("fone: ")
            print(ControllerCliente.add(nome, fone, cpf))
        # add cliente - fim

    elif op == "2":
        # exibe clientes
        print(ControllerCliente.exibe_clientes())

    elif op == "3":
        # edita cliente
        print(ControllerCliente.exibe_clientes())
        id = input("Informe o id: ")

        if ControllerCliente.verifica_se_existe_cliente(id, "id"):
            nome = input("nome ou enter: ")
            cpf = input("cpf ou enter: ")
            fone = input("fone ou enter: ")
            print("==================================")
            print(ControllerCliente.editar_cliente(id, nome, fone, cpf))

        else:
            print("Cliente nao encontrado na base de dados")

    elif op == "4":
        # excluir cliente
        print(ControllerCliente.exibe_clientes())
        id = input("Informe o id: ")

        if ControllerCliente.verifica_se_existe_cliente(id, "id"):
            print(ControllerCliente.excluir_cliente(id))

    elif op == "5":
        from view import menu_geral

        menu_geral()

    elif op == "6":
        exit()

    else:
        print("Valor invalido, retornando ao menu cliente")
        menu_cliente()
