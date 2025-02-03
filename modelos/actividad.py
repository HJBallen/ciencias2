import numpy.random as random


from constantes.constantes  import ACTIVIDADES_RUIDO

class Actividad:

  def __init__(self,nombre,descripcion) -> None:
    self.nombre = nombre
    self.descripcion = descripcion
    self.ruidoGenerado = self.determinarRuidoGenerado()

  def determinarRuidoGenerado(self):
    ruido= 0.0
    for actividad in ACTIVIDADES_RUIDO:
      if self.nombre == actividad:
        ruido = random.randint(ACTIVIDADES_RUIDO[actividad][0],ACTIVIDADES_RUIDO[actividad][1])
        break
    return ruido

