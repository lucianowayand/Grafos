import grafo_lib

class Grafo(grafo_lib.Grafo):
    def minimos_sucessores(self):
        minimos_sucessores = []

        vertice_origem = list(self.grafo.keys())[0]
        vertice = vertice_origem
        for i in range (len(self.grafo)-1):
            self.grafo[vertice]['japassei'] = 1
            print(vertice)
            aux = 9999
            
            for vertice_destino in self.grafo[vertice]['arestas']:
                if self.grafo[vertice]['arestas'][vertice_destino]['peso'] < aux and self.grafo[vertice_destino]['japassei'] == 0:
                    aux = self.grafo[vertice]['arestas'][vertice_destino]['peso']
                    menor = [vertice,vertice_destino,aux]
            
            minimos_sucessores.append(menor)
            vertice = menor[1]
        minimos_sucessores.append([vertice,vertice_origem,self.grafo[vertice]['arestas'][vertice_origem]['peso']])
        print(minimos_sucessores)

    
    def grafo_noia(self):
        self.adiciona_vertice('A')
        self.adiciona_vertice('B')
        self.adiciona_vertice('C')
        self.adiciona_vertice('D')
        self.adiciona_vertice('E')
        self.adiciona_vertice('F')

        self.adiciona_aresta_nao_direcionada_dic('A', 'B', 423)
        self.adiciona_aresta_nao_direcionada_dic('A', 'C', 501)
        self.adiciona_aresta_nao_direcionada_dic('A', 'D', 745)
        self.adiciona_aresta_nao_direcionada_dic('A', 'E', 560)
        self.adiciona_aresta_nao_direcionada_dic('A', 'F', 400)

        self.adiciona_aresta_nao_direcionada_dic('B', 'C', 425)
        self.adiciona_aresta_nao_direcionada_dic('B', 'D', 320)
        self.adiciona_aresta_nao_direcionada_dic('B', 'E', 642)
        self.adiciona_aresta_nao_direcionada_dic('B', 'F', 268)

        self.adiciona_aresta_nao_direcionada_dic('C', 'D', 232)
        self.adiciona_aresta_nao_direcionada_dic('C', 'E', 355)
        self.adiciona_aresta_nao_direcionada_dic('C', 'F', 100)

        self.adiciona_aresta_nao_direcionada_dic('D', 'E', 583)
        self.adiciona_aresta_nao_direcionada_dic('D', 'F', 330)

        self.adiciona_aresta_nao_direcionada_dic('E', 'F', 371)

    def grafo_teste(self):
        self.adiciona_vertice(0)
        self.adiciona_vertice(1)
        self.adiciona_vertice(2)
        self.adiciona_vertice(3)
        self.adiciona_aresta_nao_direcionada_dic(0, 1, 3)
        self.adiciona_aresta_nao_direcionada_dic(0, 2, 6)
        self.adiciona_aresta_nao_direcionada_dic(0, 3, 9)
        self.adiciona_aresta_nao_direcionada_dic(1, 0, 3)
        self.adiciona_aresta_nao_direcionada_dic(1, 2, 6)
        self.adiciona_aresta_nao_direcionada_dic(1, 3, 9)
        self.adiciona_aresta_nao_direcionada_dic(2, 1, 3)
        self.adiciona_aresta_nao_direcionada_dic(2, 0, 6)
        self.adiciona_aresta_nao_direcionada_dic(2, 3, 9)
        self.adiciona_aresta_nao_direcionada_dic(3, 1, 3)
        self.adiciona_aresta_nao_direcionada_dic(3, 2, 6)

    def grafo_omir(self):
        self.adiciona_vertice(0)
        self.adiciona_vertice(1)
        self.adiciona_vertice(2)
        self.adiciona_vertice(3)
        self.adiciona_vertice(4)
        self.adiciona_aresta_nao_direcionada_dic(0, 4, 1)
        self.adiciona_aresta_nao_direcionada_dic(0, 1, 1)
        self.adiciona_aresta_nao_direcionada_dic(0, 2, 5)
        self.adiciona_aresta_nao_direcionada_dic(0, 3, 2)
        self.adiciona_aresta_nao_direcionada_dic(1, 2, 1)
        self.adiciona_aresta_nao_direcionada_dic(1, 3, 2)
        self.adiciona_aresta_nao_direcionada_dic(1, 4, 3)
        self.adiciona_aresta_nao_direcionada_dic(2, 3, 1)
        self.adiciona_aresta_nao_direcionada_dic(2, 4, 1)
        self.adiciona_aresta_nao_direcionada_dic(3, 4, 2)