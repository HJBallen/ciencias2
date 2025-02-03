from modelos.planta import Planta

class Edificio:
  def __init__(self,plantas:list[Planta]) -> None:
    self.plantas = plantas
  