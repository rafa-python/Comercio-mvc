from controller.controller_funcionario import ControllerFuncionario


def menu_funcionario():
    print(
        "----==funcionario==----\n"
        "1 - add funcionario\n"
        "2 - exibir funcionarios\n"
        "3 - editar funcionario\n"
        "4 - excluir funcionario\n"
        "5 - retornar ao menu principal\n"
        "6 - sair do programa\n"
        "----==============----\n"
    )

    op = input("Escolha um numero: ")

    if op == "1":
        # add funcionario
        cpf = input("cpf: ")
        if ControllerFuncionario.verifica_se_existe(cpf, "cpf"):
            print("Funcionario ja possui cadastro")
        else:
            nome = input("nome: ")
            fone = input("fone: ")
            salario = input("salario: ")
            print(ControllerFuncionario.add(nome, fone, cpf, salario))

    elif op == "2":
        # exibir funcionario
        print(ControllerFuncionario.exibir())

    elif op == "3":
        # edita cliente
        print(ControllerFuncionario.exibir())
        id = input("Informe o id: ")

        if ControllerFuncionario.verifica_se_existe(id, "id"):
            nome = input("nome ou enter: ")
            cpf = input("cpf ou enter: ")
            fone = input("fone ou enter: ")
            salario = input("salario ou enter: ")
            print("==================================")
            print(ControllerFuncionario.edit(id, nome, fone, cpf, salario))

        else:
            print("Funcionario nao encontrado na base de dados")

    elif op == "4":
        # exclui funcionario
        print(ControllerFuncionario.exibir())
        id = input("Informe o id: ")

        if ControllerFuncionario.verifica_se_existe(id, "id"):
            print(ControllerFuncionario.excluir(id))

    elif op == "5":
        from view import menu_geral

        menu_geral()

    elif op == "6":
        exit()

    else:
        print("Valor invalido, retornando ao menu funcionarios")
        menu_funcionario()
