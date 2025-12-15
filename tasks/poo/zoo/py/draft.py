from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str):
        self.nome = nome

    def apresentar_nomes (self):
        print(f"Eu sou um animal {self.nome}")

    @abstractmethod
    def fazer_som(self):
        pass

    @abstractmethod
    def mover(self):
        pass

class Dog(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("AU AU")

    def mover(self):
        print("Dog corre atras do gato")

class Cat(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazer_som(self):
        print("MIAU")
    
    def mover(self):
        print("cat corre do dog")


def apresentar(animal: Animal):
    animal.apresentar_nomes()
    animal.fazer_som()
    animal.mover()
    print("-" * 40)

if __name__ == "__main__":
    animais = [
        Dog("Dog"),
        Cat("Cat")
    ]

    for animal in animais:
        apresentar(animal)