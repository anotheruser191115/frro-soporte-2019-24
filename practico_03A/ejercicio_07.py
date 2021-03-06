# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime
import sqlite3

from practico_03_A.ejercicio_02 import agregar_persona
from practico_03_A.ejercicio_04 import buscar_persona
from practico_03_A.ejercicio_06 import reset_tabla
from practico_03_A.ejercicio_02 import session
from practico_03_A.ejercicio_06 import PersonaPeso


def agregar_peso(id_persona, fecha, peso):
    if (buscar_persona(id_persona) == False):
        return False
    respuesta = False
    filtro=session.query(PersonaPeso).filter(PersonaPeso.idPersona==id_persona).filter(PersonaPeso.fecha>=fecha).first()
    if(filtro != None):
        return False
    else:
        x=PersonaPeso()
        x.fecha=fecha
        x.idPersona=id_persona
        x.peso=peso
        session.add(x)
        session.commit()
        return x.idPersona


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.date(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
