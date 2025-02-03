import networkx as nx
import matplotlib.pyplot as plt

from modelos.edificio import Edificio
from modelos.planta import Planta
from modelos.habitacion import Habitacion

def crear_grafo(edificio:Edificio):
  grafo = nx.Graph()
  nodos = []
  edges = []
  for planta in edificio.plantas:
    nodos = generar_nodos(planta)
  
  edges= generar_aristas(nodos)

  grafo.add_nodes_from(nodos)
  grafo.add_edges_from(edges)
  dibujar_grafo(grafo)

def generar_nodos(planta:Planta):
  nodos = []
  for habitacion in planta.habitaciones:
    nodos.append((habitacion.numero, habitacion))
  return nodos

def generar_aristas(nodos):
  edges = []
  for nodo in nodos:
    for i in range(len(nodos)-1):
      nodoJ = nodos[i]
      if nodo[1] != nodoJ[1]:
        edges.append((nodo, nodoJ ))
  return edges

def dibujar_grafo(grafo):
  pos = nx.layout.planar_layout(grafo)
  nx.draw_networkx(grafo, pos)
  plt.title("Grafo")
  plt.show()