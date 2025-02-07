from logica.logica import crear_entretenimiento, crear_deportiva, get_yeso, get_concreto, get_vidrio, crear_vivienda
from modelos.edificio import Edificio
from modelos.habitacion import Habitacion
from modelos.planta import Planta
from logica.grafo import crear_grafo, organizar_grafo

active = True
reorganizar = False

habitaciones = [Habitacion(101,crear_entretenimiento(), get_yeso()), Habitacion(102,crear_vivienda(), get_concreto()), Habitacion(103,crear_deportiva(), get_concreto()), Habitacion(104,crear_vivienda(), get_concreto())]

habitaciones2 = [Habitacion(201,crear_entretenimiento(), get_yeso()), Habitacion(202,crear_vivienda(), get_concreto()), Habitacion(203,crear_deportiva(), get_concreto()), Habitacion(204,crear_vivienda(), get_concreto())]

plantas = [Planta(habitaciones), Planta(habitaciones2)]
edificio = Edificio(plantas)

def habitabilidad():
  for planta in edificio.plantas:
    planta.generarGrafoHabitabilidad()
    for habitacion in planta.habitaciones:
      print(habitacion)
  crear_grafo(edificio)

def reorganizarGrafo():
  organizar_grafo(edificio)

1
while active:
  print("Bienvenido al sistema de determinacion de habitabilidad de un edificio")
  print("1.determinar habitabilidad")
  if reorganizar:
    print("3.Reorganizar actividades")
  print("2.salir")
  opcion = input("Ingrese una opcion: ")
  match opcion:
    case "1":
      habitabilidad()
      reorganizar = True
      pass
    case "2":
      active = False
    case "3": 
      if not reorganizar:
        break
      reorganizarGrafo()



