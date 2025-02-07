import math
from modelos.actividad import Actividad
from modelos.material import Material


yeso = Material('Yeso', 0.1)
concreto = Material('Concreto', 0.35)
vidrio = Material("Vidrio", 0.1)

def crear_vivienda():
  return Actividad('Vivienda',"Espacio residencial")

def crear_entretenimiento():
  return Actividad('Entretenimiento',"Espacio de entretenimiento")

def crear_deportiva():
  return Actividad('Deportiva',"Espacio deportivo")

def get_yeso():
  return yeso

def get_concreto():
  return concreto

def get_vidrio():
  return vidrio

def get_color(habitabilidad:str):
  match habitabilidad:
    case "Habitable":
      return "green"
    case "No habitable":
      return "red"
    case "Ruido moderado":
      return "yellow"

def get_color_actividad(nombre:str):
  match nombre:
    case "Vivienda":
      return "green"
    case "Entretenimiento":
      return "blue"
    case "Deportiva":
      return "blue"


def sumar_decibelios(db1, db2):
  return 10 * math.log10(10**(db1 / 10) + 10**(db2 / 10))