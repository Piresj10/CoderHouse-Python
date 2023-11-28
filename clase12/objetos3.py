class Animal():
    adn = True
    
    def __init__(self, cantidad_ojos: int, tipo_piel: str) -> None:
        self.cantidad_ojos = cantidad_ojos
        self.tipo_piel = tipo_piel    
    
    def respirar(self) -> int:
        #cantidad de veces que respira por minuto return: int
        
        return 30
    
    
    def correr(self) -> str:
        #me dice de que forma correr return: str
        
        return "correr normal"
class Mamifero():
    def respirar(self) -> str:
        return 'estamos respirando por la nariz'

class Gato(Mamifero, Animal):
    def __init__(self, color: str, raza: str) -> None:
        Animal.__init__(cantidad_ojos=2, tipo_piel="peludo")
        self.color = color
        self.raza = raza

class Ballena(Animal):
    def correr(self) -> str:
        return "este animal no corre"
    def nadar(self) -> str:
        return "este animal nada lento"
    
print(Animal.__mro__)
print(Gato.__mro__)




gato = Gato(color="rojo", raza="gris") 
print(gato.respirar()) 
# print(gato.raza)
# print(gato.color)
# print(gato.correr())
# print("---------------")

# ballena = Ballena(cantidad_ojos=2, tipo_piel="escamosa")
# print(ballena.correr())
# print(ballena.nadar())
