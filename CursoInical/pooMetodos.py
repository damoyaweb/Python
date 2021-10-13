#se Crea Clase Py va la primera en Mayusculas
class Carro:
    #propiedades
    marca = ''
    color = ''
    encendido = False
    velocidad = 0
    #Setearlos
    def __init__(self,marca,color):
        self.marca = marca
        self.color = color

    def encender(self):
        self.encendido = True

    def set_velocidad(self,velocidad):
        self.velocidad = velocidad
        
        
        
#Intanciar
carro1 = Carro('mercedes','negro')
carro1.encender()
carro1.set_velocidad(10)
print(f'Marca {carro1.marca}, Color {carro1.color}')

carro2 = Carro('chery','azul')
carro2.encender()
print(f'Marca {carro2.marca}, Color {carro2.color}')


if carro1.encendido:
    print(f'El Carro esta Encendido y va a una velocidad de {carro1.velocidad} km/h')
    carro1.set_velocidad(15)
    print(f'El Carro esta Encendido y va a una velocidad de {carro1.velocidad} km/h')

else:
    print('El Carro esta Apagado')
    
