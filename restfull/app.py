#importamos la libreri
from flask import Flask
import os
app = Flask(__name__)

host = 'google.com'
response = os.system("ping -c 1 " + host)

#Definir Ruta
@app.route("/ping")
#Definimos una Funcion
def index():
    if response == 0:
        return host
    else:
        return False
        


#Se inicia el Servicio
if __name__ == '__main__':
    app.run(debug=True, port=4000)