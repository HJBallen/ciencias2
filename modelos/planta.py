from constantes.constantes import MATRIZ_AD

class Planta:
  def __init__(self,habitaciones) -> None:
    self.habitaciones = habitaciones
  
  def reubicarActividades():
    pass

  def generarGrafoHabitabilidad(self):
    for i in range(4):
      if self.habitaciones[i].actividad.nombre != "Vivienda":
        print("Actividad de ruido")
        for j in range(4):
          if i == j:
            continue
          if MATRIZ_AD[i] == MATRIZ_AD[j]:
            self.habitaciones[j].recibirRuido(self.habitaciones[i].ruidoGenerado * 0.9)
          else:
            self.habitaciones[j].recibirRuido(self.habitaciones[i].ruidoGenerado * 0.4)
        for i in range(4):
            self.habitaciones[i].determinarHabitabilidad()
        return self.habitaciones
    