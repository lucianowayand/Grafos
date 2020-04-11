from leitor_de_entrada import le_entrada
from grafo_lib import Grafo

g = Grafo()

print(g.grafo)

g.adiciona_aresta_nao_direcionada(1,2)
g.elimina_aresta(2,1)

print(g.grafo)
