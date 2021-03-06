# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime
import sqlite3

from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_04 import buscar_persona
from practico_03.ejercicio_06 import reset_tabla


def agregar_peso(id_persona, fecha, peso):
    db=sqlite3.connect('mibase.db')
    cursor=db.cursor()
    if (buscar_persona(id_persona) == False):
        return False
    respuesta = False
    cadena1 = "SELECT count(*) FROM personas_peso where idPersona = ? and fecha >= ? "
    tdatos = (id_persona,fecha)
    cantidad = cursor.execute(cadena1,tdatos).fetchone()[0]
    if(cantidad == 0):
        cadena2 = "INSERT INTO personas_peso VALUES(?,?,?);"
        tdatos = (id_persona,fecha,peso)
        cursor.execute(cadena2,tdatos)
        respuesta = cursor.lastrowid
        db.commit()
    db.close()
    return respuesta


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
