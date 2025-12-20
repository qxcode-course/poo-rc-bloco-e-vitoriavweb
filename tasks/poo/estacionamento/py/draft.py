from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str, tipo: str):
        self.id = id
        self.tipo = tipo 
        self.horaentrada = None

    def setentrada (self, horaentrada: int):
        self.horaentrada = horaentrada

    def getentrada(self) -> int:
        return self.horaentrada
    
    def gettipo(self) -> str:
        return self.tipo
    
    def getid(self) -> str:
        return self.id
    
    @abstractmethod
    def calcularvalor(self, horasaida: int):
        pass

    def __str__(self):
        pass

class Bike(Veiculo):
    def __init__(self, id:str):
        super().__init__(id)

    def calcularvalor(self, horasaida):
        if self.horaentrada is None:
            print("nao bike")
        return 3.0
    
class Moto(Veiculo):
    def __init__(self, id: str):
        super().__init__(id)

    def calcularvalor(self, horasaida):
        if self.horaentrada is None:
            print("nao moto")
        tempo = (horasaida-self.horaentrada)/20
        return (tempo)
    
class Carro(Veiculo):
    def __init__(self, id:str):
        super().__init__(id )

    def calcularvalor(self, horasaida):
        if self.horaentrada is None:
            print("nao carro")
        tempo = (horasaida-self.horaentrada)/10
        if tempo <5:
            tempo=5
        return (tempo)

class Estacionamento:
    def __init__(self):
        self.veiculos = []
        self.horaatual = None

    
'''   
  
class Estacionamento:
    def __init__(self):
        self.veiculos = []
        self.horaatual = 0

    def __str__(self):
        lines = []
        for v in self.veiculos:
            tipo = v.gettipo().rjust(10, "_")
            vid  = v.getid().rjust(10, "_")
            lines.append(f"{tipo} : {vid} : {v.getentrada()}")
        lines.append(f"Hora atual: {self.horaatual}")
        return "\n".join(lines)

    def procurarveiculo(self,id:str) -> int:
        for i, v in enumerate(self.veiculos):
            if v.getid()==id:
                return i
        return -1

    def estacionar(self, veiculo: Veiculo):
        if self.procurarveiculo(veiculo.getid()) != -1:
            raise ValueError(f"{veiculo.getid()}")
        veiculo.setentrada(self.horaatual)
        self.veiculos.append(veiculo)


    def pagar(self, id:str):
        sla = self.procurarveiculo(id)
        if sla == -1:
            return
        v = self.veiculos.pop(sla)
        entrada = v.getentrada()
        saida = self.horaatual
        valor = v.calcularvalor(saida)
        print(f"{v.gettipo()} chegou {entrada} saiu {saida}. Pagar R$ {valor:.2f}")

 '''
def main():
    estacionamento = Estacionamento()

    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(estacionamento)
        elif args[0] == "tempo":
            estacionamento.horaatual += int(args[1])
        elif args[0] == "estacionar":
            tipo = args[1]
            id = args[2]

            if tipo == "bike":
                v = Bike(id)
            elif tipo == "moto":
                v = Moto(id)
            elif tipo == "carro":
                v = Carro(id)
            else:
                continue
            estacionamento.estacionar(v)
        elif args[0] == "pagar":
            id = args[1]
            estacionamento.pagar(id)


main()