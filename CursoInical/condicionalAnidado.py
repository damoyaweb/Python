#Variable
edad = int(input('Introduce tu edad: '))
mes = int(input('Introduce el numero de tu mes de naciomiento: '))

#If Anidado pero tener en cuenta que el maximo es 3
if edad >= 18:
    print('Eres Mayor de Edad')
    if mes == 1:
        print('Naci en Enero')
    elif mes == 2:
        print('Naci en Febrero')

else:
    print('Eres menor de Edad')
    if mes == 3:
        print('Naci en Marzo')
    elif mes == 4:
        print('Naci en Abril')
