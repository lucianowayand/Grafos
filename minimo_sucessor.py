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
