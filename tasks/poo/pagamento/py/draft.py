from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor: float, descricao: str):
        self.valor = valor
        self.descricao = descricao

    def validar_valor(self):
        if self.valor <= 0:
            raise ValueError("valor negativo")
        
    def resumo(self):
        return f"pagamento de R${self.valor}:{self.descricao}"

    @abstractmethod
    def processar(self):
        pass

class Cartaocredito(Pagamento):
    def __init__(self, valor:float, descricao:str, numero: str, nome_titular:str, limite_disponivel:float):
        super().__init__(valor, descricao)
        self.numero = numero
        self.nome_titular = nome_titular
        self.limite_disponivel = limite_disponivel

    def processar(self):
        if self.valor > self.limite_disponivel:
            print("PARE, sem limite irmao")
        else:
            self.limite_disponivel -= self.valor
            print(f"Pagamento feito no {self.nome_titular}\n limite: {self.limite_disponivel}"
                  )

class Pix(Pagamento):
    def __init__(self, valor:float, descricao:str, chave: str, banco:str):
        super().__init__(valor, descricao)
        self.chave = chave
        self.banco = banco
 

    def processar(self):
        print(f"pagando pix produto {self.descricao} para {self.chave} do banco {self.banco} no valor de {self.valor}")

class Boleto(Pagamento):
    def __init__(self, valor:float, descricao:str, codigo:str, vencimento:str):
        super().__init__(valor, descricao)
        self.codigo = codigo
        self.vencimento = vencimento

    def processar(self):
        print("boleto gerado. aguardando pagamento...")

pagamento = [
    Pix(150, "Camisa esportiva", "email@ex.com", "Banco XPT0"),
    Cartaocredito(400, "Tenis esportivo", "1234 5678 9123 4567", "cliente X", 500),
    Boleto(89.90, "Livro de python", "123456789000", "2025-01-10"),
    Cartaocredito(800, "Notebook", "9999 8888 7777 6666", "Cliente Y", 700)
]

def processar_pagamento(pagamento: Pagamento):
    try:
        pagamento.validar_valor()
        print(pagamento.resumo())
        pagamento.processar()
        print("-" * 50)
    except ValueError as e:
        print(f"erro: {e}")

for p in pagamento:
    processar_pagamento(p)





















        