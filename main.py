from leitor_de_entrada import le_entrada
from grafo_lib import Grafo

g = Grafo(le_entrada())

print(g.grafo)

g.adiciona_vertice('D')

g.adiciona_aresta_direcionada('D',5)
g.adiciona_aresta_direcionada('D',7)
g.elimina_aresta('D',5)

print(g.grafo)

g.elimina_vertice('A')
g.elimina_vertice('B')
g.elimina_vertice('C')
g.elimina_vertice('D')

print(g.grafo)
