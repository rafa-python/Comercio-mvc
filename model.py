from datetime import datetime


class Cliente:
    def __init__(self, nome: str, idade: int, fone: str, cpf: str):
        self.nome, self.idade, self.fone, self.cpf = nome, idade, fone, cpf


class Funcionario(Cliente):
    def __init__(self, nome: str, idade: int, fone: str, cpf: str, salario: float):
        super().__init__(nome, idade, fone, cpf)
        self.salario = salario


class Categoria:
    def __init__(self, categoria: str):
        self.categoria = categoria


class Produto:
    def __init__(self, nome: str, preco: float, categoria: Categoria):
        self.nome, self.preco, self.categoria = nome, preco, categoria


class Estoque:
    def __init__(self, produto: Produto, quantidade: int):
        self.produto, self.quantidade = produto, quantidade


class Venda:
    def __init__(
        self,
        itensVendidos: Produto,
        vendedor: Funcionario,
        comprador: Cliente,
        quantidadeVendida: int,
        date=datetime.now(),
    ):
        self.itensVendidos = itensVendidos
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidadeVendida = quantidadeVendida
        self.date = date


class Fornecedor:
    def __init__(self, nome: str, cnpj: str, fone: str, categoria: Categoria) -> None:
        self.nome, self.cnpj, self.fone, self.categoria = nome, cnpj, fone, categoria
