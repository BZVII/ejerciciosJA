'''
Debes obtener estos tres valores
   - Total de euros que se ha gastado el usuario: Es la suma de todas las cantidades_from cuando moneda_from es EUR
   - Total de euros que ha recuperado el usuario: Es la suma de todas las cantidades_to cuando moneda_to es EUR
   - Dinero aún atrapado en la inversión: Recuperado - Gastado

Tienes que hacer un programa python que acceda a la base de datos que está en este proyecto data/movimientos.db
Y te tiene que imprimir lo siguiente

+------------------------+
| Gastado...:  8305.00 € |
| Recuperado: 17512.49 € |
+------------------------+
| Atrapado..:  9207.49 € |
+------------------------+

'''

import sqlite3


def calculo1():
    conexion = sqlite3.connect("data/movimientos.db")
    cur = conexion.cursor()
    cur.execute("select sum(cantidad_from) from movimientos where moneda_from = 'EUR'")
    print(cur.description)

    filas = cur.fetchall()
    valor = filas[0][0]

    conexion.close()
    return valor

def calculo2():
    conexion = sqlite3.connect("data/movimientos.db")
    cur = conexion.cursor()
    cur.execute("select sum(cantidad_to) from movimientos where moneda_to = 'EUR'")
    print(cur.description)

    filas = cur.fetchall()
    valor = filas[0][0]
    conexion.close()
    return valor



euros_from = calculo1()
euros_to = calculo2()
atrapado = euros_to - euros_from

print("+------------------------+")
print("| Gastado...:  {} € |".format(euros_from))
print("| Recuperado: {} € |".format(euros_to))
print("+------------------------+")
print("| Atrapado..:  {} € |".format(atrapado))
print("+------------------------+")

