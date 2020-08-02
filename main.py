from leitor_de_entrada import le_entrada
from grafo_lib import Grafo
import random

g = Grafo()

g.adiciona_aresta_nao_direcionada("A","B",41)
g.adiciona_aresta_nao_direcionada("A","C",23)

print(g.grafo)
