from controller.controller_cliente import ControllerCliente
from controller.controller_funcionario import ControllerFuncionario
from controller.controller_fornecedor import ControllerFornecedor
from controller.controller_produto import ControllerProduto
from controller.controller_vendas import DaoVenda
from view_cliente import menu_cliente
from view_fornecedores import menu_fornecedor


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
            
    elif op == "14":
        print(ControllerProduto.exibe())
    
    elif op == "15":
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
                print(ControllerProduto.edit(id, nome, preco, categoria, quantidade, nome_fornecedor, id_fornecedor))
            
            elif id_fornecedor == "":
                nome_fornecedor = ""
                print(ControllerProduto.edit(id, nome, preco, categoria, quantidade, nome_fornecedor, id_fornecedor))

            else:
                print("Fornecedor nao encontrado.")

        else:
            print("Produto nao encontrado.")

    elif op == "16":
        # excluir produto
        print(ControllerProduto.exibe())
        id = input("id: ")
        if ControllerProduto.verifica_se_existe(id, "id"):
            print(ControllerProduto.excluir(id))
        else:
            print("Produto nao encontrado na base de dados.")


if __name__ == "__main__":
    menu_geral()

