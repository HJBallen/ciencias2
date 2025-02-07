from modelos.actividad import Actividad
from modelos.material import Material
from constantes.constantes  import ACTIVIDADES_HABITABILIDAD
from logica.logica import sumar_decibelios
from constantes.constantes import RECOMENDACIONES

class Habitacion:
  def __init__(self,numero, actividad:Actividad, material:Material, habitabilidad=None, ruidoRecibido = 0.0, ruidoEmitido = 0.0) -> None:
    self.numero = numero
    self.habitabilidad = habitabilidad
    self.actividad = actividad
    self.material = material
    self.ruidoRecibido = ruidoRecibido
    self.ruidoEmitido = 0.0
    self.determinarRuidoEmitido()
    self.recomendacion  = "Ninguna"
  
  def __repr__(self):
    return f"Habitacion {self.numero} Actividad: {self.actividad.nombre} Ruido Generado: {self.actividad.ruidoGenerado}, Ruido emitido: {self.ruidoEmitido}, Ruido recibido: {self.ruidoRecibido}, {self.habitabilidad}, Recomendacion: {self.recomendacion}"

  def determinarHabitabilidad(self):
    match self.actividad.nombre:
      case "Vivienda":
        if self.ruidoRecibido > ACTIVIDADES_HABITABILIDAD["Vivienda"][1] :
          self.habitabilidad = "No habitable"
          self.recomendacion = RECOMENDACIONES["Costosa"]
        if self.ruidoRecibido >ACTIVIDADES_HABITABILIDAD["Vivienda"][0] and self.ruidoRecibido <= ACTIVIDADES_HABITABILIDAD["Vivienda"][1]:
          self.habitabilidad = "Ruido moderado"
          self.recomendacion = RECOMENDACIONES["Economica"]
        if self.ruidoRecibido <= ACTIVIDADES_HABITABILIDAD["Vivienda"][0]:
          self.habitabilidad = "Habitable"
      case "Entretenimiento":
        if self.ruidoRecibido > ACTIVIDADES_HABITABILIDAD["Entretenimiento"][1] :
          self.habitabilidad = "No habitable"
          self.recomendacion = RECOMENDACIONES["Costosa"]
        if self.ruidoRecibido >ACTIVIDADES_HABITABILIDAD["Entretenimiento"][0] and self.ruidoRecibido <= ACTIVIDADES_HABITABILIDAD["Entretenimiento"][1]:
          self.habitabilidad = "Ruido moderado"
          self.recomendacion = RECOMENDACIONES["Economica"]
        if self.ruidoRecibido <= ACTIVIDADES_HABITABILIDAD["Entretenimiento"][0]:
          self.habitabilidad = "Habitable"
      case "Deportiva":
        if self.ruidoRecibido > ACTIVIDADES_HABITABILIDAD["Deportiva"][1] :
          self.habitabilidad = "No habitable"
          self.recomendacion = RECOMENDACIONES["Costosa"]
        if self.ruidoRecibido >ACTIVIDADES_HABITABILIDAD["Deportiva"][0] and self.ruidoRecibido <= ACTIVIDADES_HABITABILIDAD["Deportiva"][1]:
          self.habitabilidad = "Ruido moderado"
          self.recomendacion = RECOMENDACIONES["Economica"]
        if self.ruidoRecibido <= ACTIVIDADES_HABITABILIDAD["Deportiva"][0]:
          self.habitabilidad = "Habitable"
    pass

  def determinarRuidoEmitido(self):
    self.ruidoEmitido = self.actividad.ruidoGenerado * (1-self.material.reduccionRuido)

  def recibirRuido(self,ruido):
    if self.ruidoRecibido == 0.0:
      self.ruidoRecibido = self.actividad.ruidoGenerado
    ruidoReducido = ruido * (1-self.material.reduccionRuido)
    self.ruidoRecibido = sumar_decibelios(self.ruidoRecibido, ruidoReducido)