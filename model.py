from datetime import datetime


class Cliente:
    def __init__(self, nome: str, fone: str, cpf: str):
        self.nome, self.fone, self.cpf = nome, fone, cpf


class Funcionario(Cliente):
    def __init__(self, nome: str, fone: str, cpf: str, salario: float):
        super().__init__(nome, fone, cpf)
        self.salario = salario


class Fornecedor:
    def __init__(self, nome: str, cnpj: str, fone: str):
        self.nome, self.cnpj, self.fone, self.categoria = nome, cnpj, fone


class Produto:
    def __init__(
        self,
        nome: str,
        preco: float,
        categoria: str,
        quantidade: int,
        fornecedor: str,
    ):
        self.nome, self.preco, self.categoria, self.quantidade, self.fornecedor = (
            nome,
            preco,
            categoria,
            quantidade,
            fornecedor,
        )


class Venda:
    def __init__(
        self,
        itensVendidos: Produto,
        vendedor: Funcionario,
        comprador: Cliente,
        quantidadeVendida: int,
        date=datetime.now().strftime("d/%m/%Y"),
    ):
        self.itensVendidos = itensVendidos
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidadeVendida = quantidadeVendida
        self.data = date
