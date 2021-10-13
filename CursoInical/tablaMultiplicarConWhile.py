table = int(input('Que tabla quieres ver: '))
count = 1
while count <= 10:
    result = table * count
    print(f'{table} X {count} = {result}')
    count = count + 1