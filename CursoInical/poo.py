#se Crea Clase Py va la primera en Mayusculas
class Carro:
    #propiedades
    marca = ''
    color = ''
    #Setearlos
    def __init__(self,marca,color):
        self.marca = marca
        self.color = color
        
#Intanciar
carro1 = Carro('mercedes','negro')
carro2 = Carro('chery','azul')

print(f'Marca {carro1.marca}, Color {carro1.color}')
print(f'Marca {carro2.marca}, Color {carro2.color}')



