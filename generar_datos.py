from random import randint, choice
from vector import Vector

def generar_data(puntos, rango):
    datos = []
    for _ in range(puntos):
        x = randint(0, rango) * choice([1, -1])
        y = randint(0, rango) * choice([1, -1])
        datos.append(Vector(x,y))

    return datos