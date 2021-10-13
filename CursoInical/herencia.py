"""
herencia -> para heredar atributos de una clase se debe crear la clase especifica
"""

#se Crea Clase Py va la primera en Mayusculas
class Carro:
    #propiedades
    marca = ''
    color = ''
    #Para encapsular se debe poner __antes de la propiedad
    __encendido = False
    velocidad = 0
    #Setearlos
    def __init__(self,marca,color):
        self.marca = marca
        self.color = color

    def encender(self):
        self.__encendido = True

    def set_velocidad(self,velocidad):
        self.velocidad = velocidad
    
    def get_encendido(self):
        return self.__encendido

#para heredar la clase padre se debe crear la clase hijo y con () llamar la clase padre
class CarroDeportivo(Carro):
    cv = 60

    def __init__(self, marca, color,cv):
        self.marca = marca
        self.color = color
        self.cv = cv       

#Instanciar
carro1 = Carro('mercedes','negro')
carro1.encender()
carro1.set_velocidad(10)
print(carro1.get_encendido())
print(f'Marca {carro1.marca}, Color {carro1.color}')

#instanciar carroDeportivo
carroDep = CarroDeportivo('BMW','Amarillo',200)
print(f'Marca {carroDep.marca}, Color {carroDep.color}, Cv: {carroDep.cv}')