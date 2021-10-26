import pyodbc

#instancia de Coneccion
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=GWS-BOG113\SQLEXPRESS;DATABASE=TarjetaCreditoDb;Trusted_Connection=yes;')

#Crear el objeto Conector
cursor = connection.cursor()

cursor.execute('select * from TarjetaCreditoDb')
row = cursor.fetchone()

while row:
    print(row[1])
    row = cursor.fetchone()



cursor.close()
connection.close()