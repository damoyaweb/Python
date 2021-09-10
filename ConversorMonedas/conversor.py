def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos Pesos " + tipo_pesos + " Tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $ " + dolares + " dolares")

menu = """
Bienvenido al Conversor de Monedas 💰

1 - Pesos Colombianos
2 - Pesos Mexicanos
3 - Pesos Argentinos

Elige una opcion: """

opcion = int(input(menu))
if opcion == 1:
    conversor("Colombianos",3875)
elif opcion == 2:
    conversor("Argentinos", 65)
elif opcion == 3:
    conversor("Mexicanos", 24)
else:
    print("Seleccione un Opcion")