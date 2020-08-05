from leitor_de_entrada import le_entrada
from grafo_lib import Grafo


g = Grafo()

g.cria_grafo_aleatorio(50)
print(g.grafo)

g.cria_graphviz()
