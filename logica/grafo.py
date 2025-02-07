import networkx as nx
import matplotlib.pyplot as plt

from modelos.edificio import Edificio
from modelos.planta import Planta
from modelos.habitacion import Habitacion
from logica.logica import get_color, get_color_actividad

def crear_grafo(edificio:Edificio):
  grafo = nx.Graph()
  nodos = []
  edges = []
  for planta in edificio.plantas:
    generar_nodos(planta,nodos)
  edges= generar_aristas(nodos)

  grafo.add_nodes_from([(nodo[0], {'color': nodo[1]}) for nodo in nodos])
  grafo.add_edges_from(edges)
  dibujar_grafo(grafo)

def organizar_grafo(edificio:Edificio):
  grafo = nx.Graph()
  nodos = []
  edges = []
  for planta in edificio.plantas:
    organizar_nodos(planta,nodos)
  nodos = reubicar_nodos(nodos)
  edges= generar_aristas(nodos)
  grafo.add_nodes_from([(nodo[0], {'color': nodo[1]}) for nodo in nodos])
  grafo.add_edges_from(edges)
  dibujar_grafo(grafo)

def generar_nodos(planta:Planta, nodos:list):
  for habitacion in planta.habitaciones:
    nodos.append((habitacion.numero, get_color(habitacion.habitabilidad)))

def organizar_nodos(planta:Planta, nodos:list):
  for habitacion in planta.habitaciones:
    nodos.append((habitacion.numero, get_color_actividad(habitacion.actividad.nombre)))

def reubicar_nodos(nodos:list):
  pisos = {}
  contador = 1
  newList = []

  for nodo in nodos:
    if nodo[1] not in pisos:
      pisos[nodo[1]] = [nodo]
      continue
    else:
      pisos[nodo[1]].append(nodo)
  for clave, lista in pisos.items():
    i = 1
    for j in range(len(lista)):
      nodoList = list(lista[j])
      nodoList[0] = (contador*100) + i
      lista[j] = tuple(nodoList)
      i+=1
    contador+=1

  for lista in pisos.values():
    newList.extend(lista)
  return newList
  


def generar_aristas(nodos):
  edges = []
  for i in range(len(nodos)):
    for j in range(i + 1, len(nodos)):
      num1, num2 = str(nodos[i][0]), str(nodos[j][0])  # Convertimos a string para comparar dígitos
      if (num1[0] == num2[0]) or (num1[-1] == num2[-1]):  # Mismo primer dígito (piso) o mismo último dígito
        edges.append((nodos[i][0], nodos[j][0]))  
  return edges

def dibujar_grafo(grafo):
  pos = nx.circular_layout(grafo)
  node_colors = [grafo.nodes[nodo]['color'] for nodo in grafo.nodes()]
  nx.draw_networkx(grafo, pos, node_color = node_colors, with_labels=True, labels = {nodo: nodo for nodo in grafo.nodes()})
  plt.title("Grafo")
  plt.show()