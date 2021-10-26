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

class CarroDeportivo(Carro):
    cv = 60

    def __init__(self, marca, color,cv):
        self.marca = marca
        self.color = color
        self.cv = cv       