from leitor_de_entrada import le_entrada
from grafo_lib import Grafo
   
#Cria um grafo aleatorio e o categoriza de acordo com o BFS
g = Grafo()
g.cria_grafo_aleatorio(30)
g.iniciarBFS()
g.cria_graphviz()
