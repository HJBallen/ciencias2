import numpy.random as random

from constantes.constantes  import ACTIVIDADES

class Actividad:

  def __init__(self,nombre,descripcion) -> None:
    self.nombre = nombre
    self.descripcion = descripcion
    self.ruidoGenerado = self.determinarRuidoGenerado()

  def determinarRuidoGenerado(self):
    ruido= 0.0
    for actividad in ACTIVIDADES:
      print(actividad)
      if self.nombre == actividad:
        ruido = random.randint(ACTIVIDADES[actividad][0],ACTIVIDADES[actividad][1])
        break
    return ruido


prueba = Actividad("Vivienda","a")
print(prueba.determinarRuidoGenerado())

