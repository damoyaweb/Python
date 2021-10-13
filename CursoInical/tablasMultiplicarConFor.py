table = int(input('Que tabla quieres ver: '))
mumeros = range(0,112)

for num in mumeros:
    result = table * num
    print(f'{table} X {num} = {result}')

    