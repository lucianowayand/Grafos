from leitor_de_entrada import le_entrada
from grafo_lib import Grafo

g = Grafo()

g.cria_grafo_aleatorio(2)
g.adiciona_aresta_nao_direcionada(0, 1, 100)
g.adiciona_aresta_nao_direcionada(1, 2, 200)
print(g.grafo)
g.elimina_vertice(0)
print(g.grafo)
