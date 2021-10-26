#Sobrescribir - w
#escribir - a
#leer - r

#Sobrescribir
"""f = open('archivo.txt','w+')
for i in range(0,10):
    f.write('Hola\n')"""

#Escribir
"""f = open('archivo.txt','a+')
for i in range(0,10):
    f.write('Adios\n')"""

#Leer
f = open('416820.json','r+')
datos = f.read()
print(datos)
f.close