from grafo_lib import Grafo

# Cria um grafo aleatorio e o categoriza de acordo com o BFS
g = Grafo()
g.adiciona_vertice('A')
g.adiciona_vertice('B')
g.adiciona_vertice('C')
g.adiciona_vertice('D')
g.adiciona_aresta_nao_direcionada_dic('A', 'B', 1)
g.adiciona_aresta_nao_direcionada_dic('A', 'C', 1)
g.adiciona_aresta_nao_direcionada_dic('A', 'D', 1)
g.adiciona_aresta_nao_direcionada_dic('B', 'C', 1)
g.adiciona_aresta_nao_direcionada_dic('B', 'D', 1)
g.adiciona_aresta_nao_direcionada_dic('C', 'D', 1)

# g.ord_pesos_das_arestas()
g.dfs([],'A')
# g.cria_graphviz_tb2()


