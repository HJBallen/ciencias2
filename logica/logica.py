import math

def sumar_decibelios(db1, db2):
  return 10 * math.log10(10**(db1 / 10) + 10**(db2 / 10))