from modelos.actividad import Actividad
from modelos.material import Material
from logica.logica import sumar_decibelios

class Habitacion:
  def __init__(self,numero, actividad:Actividad, material:Material, habitabilidad=None, ruidoRecibido = 0.0, ruidoEmitido = 0.0) -> None:
    self.numero = numero
    self.habitabilidad = habitabilidad
    self.actividad = actividad
    self.material = material
    self.ruidoRecibido = ruidoRecibido
    self.ruidoEmitido = ruidoEmitido
  
  def __repr__(self):
    return f"Habitacion {self.numero} Actividad{self.actividad.nombre} Ruido Generado: {self.actividad.ruidoGenerado}, Ruido emitido: {self.ruidoGenerado} Ruido recibido: {self.ruidoRecibido}, {self.habitabilidad}"

  def determinarHabitabilidad(self):
    match self.actividad.nombre:
      case "Vivienda":
        if self.ruidoRecibido > 6.4:
          self.habitabilidad = "No habitable"
        if self.ruidoRecibido < 6.5 and self.ruidoRecibido > 5:
          self.habitabilidad = "Ruido moderado"
      case "Musica":
                pass
      case "Deporte":
                pass
      case "Entretenimiento":
        pass
    pass

  def determinarRuidoEmitido(self):
    self.ruidoEmitido = self.actividad.ruidoGenerado * self.material.reduccionRuido

  def recibirRuido(self,ruido):
    if self.ruidoRecibido == 0.0:
      self.ruidoRecibido = self.actividad.ruidoGenerado
    ruidoReducido = ruido * self.material.reduccionRuido
    self.ruidoRecibido = sumar_decibelios(self.ruidoRecibido, ruidoReducido)