#defaultdict e uma funcao importante para o inicio de um dicionario vazio.
from collections import defaultdict

#As bibliotecas random e math, são utilizadas no posicionamento e calculo de K(log)
import random
import math

#Graphviz e utilizado para formar a representação gráfica abaixo se configura o grafo a ser representado
#de modo a determinar o formato, sua construção e método de inserção.
from graphviz import Graph
dot = Graph('Grafo', format='png', engine='fdp', strict=True)


class Grafo():
    # Funcao construtora que pode ou nao receber o grafo pre determinado.
    def __init__(self, grafo=defaultdict(dict)):
        # Caso não receba um grafo se inicia um dicionario vazio, caso contrario se insere o valor recebido.
        self.grafo = grafo

    # Esta funcao adiciona vertices vazios.
    def adiciona_vertice_vazio(self, vertice, x, y):
        # Caso nao exista o vertice ele sera iniciado com uma lista vazia ou reinicia as informações de um vertice existente.
        self.grafo[vertice] = {'coordenadas': {'X': x, 'Y': y}, 'arestas': {}}

    # Funcao para adicionar arestas com origem e destino bem determinados.
    def adiciona_aresta_direcionada(self, vertice_origem, vertice_destino, peso):
        # Checa a existencia dos vertices antes de conecta-los.
        if vertice_origem in self.grafo:
            if vertice_destino in self.grafo:
                self.grafo["arestas"].update({vertice_destino: peso})
            else:
                print("\033[31mNão há vertice destino\033[m")
        else:
            print("\033[31mNão há vertice origem\033[m")

    # Funcao para adicionar arestas com origem e destino bem determinados.
    def adiciona_aresta_nao_direcionada(self, vertice_origem, vertice_destino, peso):
        if vertice_origem in self.grafo:
            if vertice_destino in self.grafo:
                self.grafo[vertice_origem]["arestas"].update({vertice_destino: peso})
                self.grafo[vertice_destino]["arestas"].update({vertice_origem: peso})
            else:
                print("\033[31mNão há vertice destino\033[m")
        else:
            print("\033[31mNão há vertice origem\033[m")

    # Funcao para remover arestas entre dois vertices.
    def elimina_aresta(self, vertice_origem, vertice_destino):
        if vertice_origem in self.grafo:
            try:
                del self.grafo[vertice_origem]["arestas"][vertice_destino]
                del self.grafo[vertice_destino]["arestas"][vertice_origem]
            except:
                print("Nao existe conexao de", vertice_origem, "a", vertice_destino)

    # Funcao para a remocao de vertices.
    def elimina_vertice(self, vertice):
        # Caso exista ele sera removido.
        if vertice in self.grafo:
            # Percorre-se todo o grafo buscando as referencias ao vertice a ser removido.
            for key in self.grafo:
                # Para o caso de mais uma conexao ao mesmo vertice se removem todas as conexoes ate nao existir mais conexao determinada
                while vertice in self.grafo[key]["arestas"]:
                    print(vertice)
                    self.elimina_aresta(key, vertice)
            del self.grafo[vertice]

    # Funcao simples para simplificar o código e deixa-lo mais legivel.
    def distancia_de_vertices(self, a, b):
        return round(((self.grafo[a]["coordenadas"]["X"] - self.grafo[b]["coordenadas"]["X"])**2 + (self.grafo[a]["coordenadas"]["Y"] - self.grafo[b]["coordenadas"]["Y"])**2)**0.5, 2)

    def cria_grafo_aleatorio(self, numero_de_vertices):
        # Cria e adiciona todos os vertices com os valores de x e y já definidos
        for i in range(numero_de_vertices):
            self.adiciona_vertice_vazio(
                i, round(random.random(), 4), round(random.random(), 4))

        # Adiciona as arestas entre os vertices, os vizinhos de cada vertice sao apenas os K pontos mais proximos, onde K = parte inteira de log2(n)
        k = math.floor(math.log(numero_de_vertices, 2))
        
        for vertices in self.grafo:
            
            vertices_mais_proximos = []
            
            for i in range(k): # Insere k vertices em sua lista de vizinhos
                vertices_mais_proximos.append(0) # Embromation para solucionar o erro de array out of index
                aux = 99 # Numero representativo maior que 1.
                
                for __vertices in self.grafo: # Verifica para todos os vertices no grafo:
                    if __vertices in vertices_mais_proximos or __vertices == vertices: #Se ja fazem parte da lista de vertices proximos, pulando o caso de si mesmo.
                        pass
                    
                    else: #Ou se a distancia do vertice é inferior ao menor que havia encontrado, excluso os casos acima descritos.
                        if aux > self.distancia_de_vertices(vertices, __vertices):
                            aux = self.distancia_de_vertices(vertices, __vertices)
                            vertices_mais_proximos[i] = __vertices

            for vertices_proximos in vertices_mais_proximos: #Adiciona-se aresta entre os vertices mais proximos e o vertice, com peso determinado pela distancia.
                self.adiciona_aresta_nao_direcionada(vertices, vertices_proximos, self.distancia_de_vertices(vertices, vertices_proximos))

    
    def cria_graphviz(self):
        for vertice1 in self.grafo:#Percorre o grafo incluindo os vertices
            dot.node(str(vertice1), pos=str(self.grafo[vertice1]['coordenadas']['X'])+','+str(self.grafo[vertice1]['coordenadas']['Y'])+'!')
            for vertice2 in self.grafo[vertice1]['arestas']:
                # Preparacao para printar só a aresta de ida e nao a de volta
                self.grafo[vertice1]['arestas'][vertice2] = {'jaPassei': 0}

        for vertice1 in self.grafo:#Depois conecta os vertices com as arestas determinadas
            for vertice2 in self.grafo[vertice1]['arestas']:
                if self.grafo[vertice1]['arestas'][vertice2]['jaPassei'] == 0:
                    self.grafo[vertice1]['arestas'][vertice2]['jaPassei'] = 1
                    self.grafo[vertice2]['arestas'][vertice1]['jaPassei'] = 1
                    dot.edge(str(vertice1), str(vertice2))

        #Cria o arquivo do grafo
        dot.render('test-output/grafo')

    def bfss(self, f, t, grafo):
        while f != []:
            v = f[0]
            del f[0]
            for w in grafo[v]['arestas']:
                if grafo[w]['indice'] == 0:
                    grafo[w]['pai'] = v
                    grafo[w]['nivel'] = grafo[v]['nivel'] + 1
                    t += 1
                    grafo[w]['indice'] = t
                    f.append(w)
                elif grafo[w]['nivel'] == grafo[v]['nivel']:
                    if grafo[w]['pai'] == grafo[v]['pai']:
                        dot.edge(str(v), str(w), color='red')
                    else:
                        #dot.edge(str(v), str(w), color='')
                        pass
                elif grafo[w]['nivel'] == grafo[v]['nivel'] + 1:
                    dot.edge(str(v), str(w), color='green')

    def iniciarBFS(self): #Funcao de preparação, copia o grafo em um auxiliar de tratamento
        #Inicialização de valores
        grafo_bfs = self.grafo
        t = 0
        f = []
        self.aquarela() #Pinta o grafo raiz para mudar as cores a cada interação.

        for vertice in grafo_bfs:
            grafo_bfs[vertice]['indice'] = 0
            grafo_bfs[vertice]['pai'] = None
        
        for _vertice in grafo_bfs:  # Para que a busca atinja todos os vértices, no caso de G ser desconexo: acesso = 0;
            grafo_bfs[_vertice]['nivel'] = 0
            t += 1
            grafo_bfs[_vertice]['indice'] = t
            f.append(_vertice)
            self.bfss(f, t, grafo_bfs)

        print(grafo_bfs, end='\n')
        print(f)

    def aquarela(self):
        dot.node('0', fillcolor='orange', style='filled')
        for vertice1 in self.grafo:
            for vertice2 in self.grafo[vertice1]['arestas']:
                if vertice1 == 0 or vertice2 == 0:
                    pass
                else:
                    dot.edge(str(vertice1), str(vertice2), color='yellow')
