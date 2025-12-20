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
        sla = self.horaentrada if self.horaentrada is not None else "-"
        return f"{self.tipo} : {self.id} : {sla}"

class Bike(Veiculo):
    def __init__(self, id:str):
        super().__init__(id, "Bike")

    def calcularvalor(self, horasaida):
        if self.horaentrada is None:
            print("nao bike")
        return 3.0
    
class Moto(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Moto")

    def calcularvalor(self, horasaida):
        if self.horaentrada is None:
            print("nao moto")
        tempo = (horasaida-self.horaentrada)/20
        return (tempo)
    
class Carro(Veiculo):
    def __init__(self, id:str):
        super().__init__(id, "Carro" )

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
        self.horaatual = 0

    def procurar(self, id:str)->int:
        for i, c in enumerate(self.veiculos):
            if c.getid() == id:
                return i
        return -1 
    
    def estacionar(self, veiculo: Veiculo):
        if self.procurar(veiculo.getid()) != -1:
            return
        veiculo.setentrada(self.horaatual)
        self.veiculos.append(veiculo)

    def pagar(self,id:str):
        pag = self.procurar(id)
        if pag == -1:
            return
        c = self.veiculos.pop(pag)
        entrada = c.getentrada()
        saida = self.horaatual
        valor = c.calcularvalor(saida)
        print(f"{c.gettipo()} chegou {entrada} saiu {saida}. Pagar R$ {valor:.2f}")

    def __str__(self):
        lines = []
        for c in self.veiculos:
            tipo = c.gettipo().rjust(10).replace(" ", "_")
            vid = c.getid().rjust(10).replace(" ", "_")
            ent = str(c.getentrada()).rjust(2)
            lines.append(f"{tipo} : {vid} : {ent}")

        lines.append(f"Hora atual: {self.horaatual}")
        return "\n".join(lines)   
        

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
        elif args[0] == "estacionar":
            tipo = args[1]
            id = args[2]

            if tipo == "bike":
                c = Bike(id)
            elif tipo == "moto":
                c = Moto(id)
            elif tipo == "carro":
                c = Carro(id)
            else: 
                continue
            estacionamento.estacionar(c)
        elif args[0] == "tempo":
            estacionamento.horaatual += int(args[1])
        elif args[0] == "pagar":
            id = args[1]
            estacionamento.pagar(id)

main()