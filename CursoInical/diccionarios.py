#Crecion de un Diccionario
data = {'name':'Diego','last_name':'Moya','edad':'35'}
#Acceder a todo el diccionario
print(data)
#Accefer a un dato en especificio
print(data['last_name'])

#añadir un nuevo dato
print(data)
data['city'] = 'Bogota'
print(data)

#eliminar un dato
print(data)
del data['edad']
print(data)

#saber cuantas claves hay
print(len(data))