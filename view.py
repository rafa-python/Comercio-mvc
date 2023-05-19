from controller import *

def menu():
    print(
        "----==Menu==----\n"
        "1 - add cliente\n"
        "2 - exibir clientes\n"
        "3 - editar cliente\n"
        "4 - excluir cliente\n"
        "------------------\n"
        "5 - add fornecedor\n"
        "6 - exibir fornecedor\n"
        "7 - editar fornecedor\n"
        "8 - excluir fornecedor\n"
        "------------------\n"
        "9 - add funcionario\n"
        "10 - exibir funcionario\n"
        "11 - editar funcionario\n"
        "12 - excluir funcionario\n"
        "------------------\n"
        "13 - add produto\n"
        "------------------\n"
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
        cnpj = input("cnpj: ")
        if ControllerFornecedor.verifica_se_existe_fornecedor(cnpj, "cnpj"):
            print("Fornecedor ja possui cadastro")
        else:
            nome = input("nome: ")
            fone = input("fone: ")
            print(ControllerFornecedor.add_fornecedor(nome, cnpj, fone))

    elif op == "6":

        print(ControllerFornecedor.exibe_fornecedores())

    elif op == "7":
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
    
    elif op == "8":
        # excluir fornecedor
        print(ControllerFornecedor.exibe_fornecedores())
        id = input("Informe o id: ")

        if ControllerFornecedor.verifica_se_existe_fornecedor(id, "id"):
            print(ControllerFornecedor.excluir(id))
    
    elif op == "9":
        # add funcionario
        cpf = input("cpf: ")
        if ControllerFuncionario.verifica_se_existe(cpf, "cpf"):
            print("Funcionario ja possui cadastro")
        else:
            nome = input("nome: ")
            fone = input("fone: ")
            salario = input("salario: ")
            print(ControllerFuncionario.add(nome, fone, cpf, salario))

    elif op == "10":
        # exibir funcionario
        print(ControllerFuncionario.exibir())

    elif op == "11":
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

    elif op == "12":
        # exclui funcionario
        print(ControllerFuncionario.exibir())
        id = input("Informe o id: ")

        if ControllerFuncionario.verifica_se_existe(id, "id"):
            print(ControllerFuncionario.excluir(id))

    elif op == "13":
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
                print(ControllerProduto.add(nome, preco, categoria, quantidade, nome_fornecedor, id_fornecedor))
            
            else:
                print("Fornecedor nao encontrado.")
            



if __name__ == "__main__":
    menu()

