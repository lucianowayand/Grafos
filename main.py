from leitor_de_entrada import le_entrada
from grafo_lib import Grafo
import random

g = Grafo()

g.adiciona_vertice_vazio("Coco",72,0)
g.adiciona_vertice_vazio("Cuscus",64,12)
g.adiciona_aresta_nao_direcionada("Coco","Cuscus","72 kg")

print(g.grafo)
