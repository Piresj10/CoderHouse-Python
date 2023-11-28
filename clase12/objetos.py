class Dog:
    #atributros de clase
    tipo = "mamifero"
    cantidad_ojos = 2
    
#_ protegido
#__ privado
#+ publico
   
    def __len__(self):
        return len(self._raza)
    
    ##atributos de instancia
    def __init__(self, raza: str, color: str) -> None:
        self._raza = raza
        self.color = color

    
    #atributos de funciones
    def _ladrar(self) -> str:
        if self._raza == "doberman":
            return "ggggggggrrr"
        return "wofff"
    
    #@staticmethod sirve para no instanciar
    def caminar(self, cantidad_pasos):
        if cantidad_pasos > 100:
            return "ha caminado mucho"
        return "ha caminado poco"

dog_1 = Dog(raza="doberman", color="negro")
print(dog_1._raza)
print(dog_1.color)
print(dog_1._ladrar())
print("___________")

dog_2 = Dog(raza="husky", color="gris")
print(dog_2._raza)
print(dog_2.color)
print(dog_2._ladrar())
print(dog_1.caminar(50))
print(len(dog_1))