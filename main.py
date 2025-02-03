from modelos.actividad import Actividad
from modelos.edificio import Edificio
from modelos.habitacion import Habitacion
from modelos.material import Material
from modelos.planta import Planta

from logica.grafo import crear_grafo

vivienda = Actividad('Vivienda',"Espacio residencial")
deportiva= Actividad('Deportiva',"Espacio residencial")
entretenimiento = Actividad('Entretenimiento',"Espacio residencial")

yeso = Material('Yeso', 0.1)
concreto = Material('Concreto', 0.5)
vidrio = Material("Vidrio", 0.25)

habitaciones = [Habitacion(101,entretenimiento, yeso), Habitacion(102,vivienda, vidrio), Habitacion(103,entretenimiento, concreto), Habitacion(104,vivienda, concreto)]

plantas = [Planta(habitaciones)]

edificio = Edificio(plantas)

for planta in edificio.plantas:
  planta.generarGrafoHabitabilidad()

for habitacion in planta.habitaciones:
  print(habitacion)
crear_grafo(edificio)




