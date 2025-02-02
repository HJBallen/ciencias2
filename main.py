from modelos.actividad import Actividad
from modelos.edificio import Edificio
from modelos.habitacion import Habitacion
from modelos.material import Material
from modelos.planta import Planta

from logica.grafo import crear_grafo

vivienda = Actividad('Vivienda',"Espacio residencial")
deportiva= Actividad('Deportiva',"Espacio residencial")
entretenimiento = Actividad('Entretenimiento',"Espacio residencial")

habitaciones = [Habitacion(101,vivienda), Habitacion(102,deportiva), Habitacion(103,entretenimiento), Habitacion(104,vivienda)]

plantas = [Planta(habitaciones)]

edificio = Edificio(plantas)

print(edificio.plantas)

crear_grafo(edificio)

