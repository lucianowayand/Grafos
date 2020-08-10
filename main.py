from leitor_de_entrada import le_entrada
from grafo_lib import Grafo


g = Grafo()

g.cria_grafo_aleatorio(5)
print(g.grafo, end='\n\n\n')
# g.bfs()
g.cria_graphviz()
