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
        "----========----\n"
        )

    op = input("Escolha um numero: ")

    if op == "1":
        # add cliente
        cpf = input("cpf: ")
        if ControllerCliente.verifica_se_existe_cliente(cpf, "cpf", "Cliente"):
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

if __name__ == "__main__":
    menu()

