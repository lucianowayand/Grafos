from grafo_lib import Grafo

# Cria um grafo aleatorio e o categoriza de acordo com o BFS
g = Grafo()
g.adiciona_vertice(0)
g.adiciona_vertice(1)
g.adiciona_vertice(2)
g.adiciona_vertice(3)
g.adiciona_vertice(4)
g.adiciona_aresta_nao_direcionada_dic(0, 4, 1)
g.adiciona_aresta_nao_direcionada_dic(0, 1, 1)
g.adiciona_aresta_nao_direcionada_dic(0, 2, 5)
g.adiciona_aresta_nao_direcionada_dic(0, 3, 2)
g.adiciona_aresta_nao_direcionada_dic(1, 2, 1)
g.adiciona_aresta_nao_direcionada_dic(1, 3, 2)
g.adiciona_aresta_nao_direcionada_dic(1, 4, 3)
g.adiciona_aresta_nao_direcionada_dic(2, 3, 1)
g.adiciona_aresta_nao_direcionada_dic(2, 4, 1)
g.adiciona_aresta_nao_direcionada_dic(3, 4, 2)

# g.ord_pesos_das_arestas()
g.dfs(0)
# g.cria_graphviz_tb2()


