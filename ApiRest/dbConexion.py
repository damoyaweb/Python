import pyodbc
try:
    connetion=pyodbc.connect('DRIVER={SQL Server};SERVER=GWS-BOG113\SQLEXPRESS;DATABASE=Inventario;Trusted_Connetion=yes;')
except conetion:
    pass