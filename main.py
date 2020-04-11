from leitor_de_entrada import le_entrada
from grafo_lib import Grafo

g = Grafo(le_entrada())

print(g.grafo)

g.elimina_vertice('V3')

print(g.grafo)

#Testando commit direto do vsc