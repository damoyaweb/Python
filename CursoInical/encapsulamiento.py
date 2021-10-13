"""
encapsulamiento -> solo se puede acceder mediante metodos creados previamente
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

        
#Intanciar
carro1 = Carro('mercedes','negro')
carro1.encender()
carro1.set_velocidad(10)

print(carro1.get_encendido())
