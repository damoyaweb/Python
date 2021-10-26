import json

class Lineas:
    id = 0
    idSolicitud = 0
    linenum = 0

    def __init__(self,id,idSoliciutd,linenum):
        self.id = id
        self.idSolicitud = idSoliciutd
        self.linenum = linenum


#Traer el Archivo jso
f = open('416820.json')

#Cargar Datos a una Variable
data = json.load(f)

#iteramos el archiv
datosLineas = Lineas()

for i in data['lineas']:
    datosLineas.id = i['id']
    datosLineas.linenum = i['linenum']
    datosLineas.idSolicitud = i['idSolicitud']
    print(datosLineas)
f.close
    