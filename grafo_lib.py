# defaultdict e uma funcao importante para o inicio de um dicionario vazio.
from collections import defaultdict
import random
import math


class Grafo():
    # Funcao construtora que pode ou nao receber o grafo pre determinado, o ideal e utilizar a funcao le_entrada para o tal.
    def __init__(self, grafo=defaultdict(dict)):
        # Caso não receba um grafo se inicia um dicionario vazio, caso contrario se insere o valor recebido.
        self.grafo = grafo

    # Esta funcao adiciona vertices vazios.
    def adiciona_vertice_vazio(self, vertice, x, y):
        # Caso nao exista o vertice ele sera iniciado com uma lista vazia ou atualiza informações de um vertice existente.
        self.grafo[vertice] = {'coordenadas': {'X': x, 'Y': y}, 'arestas': {}}

    # Funcao para adicionar arestas com origem e destino bem determinados.
    def adiciona_aresta_direcionada(self, vertice_origem, vertice_destino, peso):
        # Caso ja exista o vertice esta conexao sera feita ao fim da lista.
        if vertice_origem in self.grafo:
            if vertice_destino in self.grafo:
                self.grafo["arestas"].update({vertice_destino: peso})
            else:
                print("\033[31mNão há vertice destino\033[m")
        # Caso ainda nao exista esse vertice se inicia uma lista apenas com seu valor.
        else:
            print("\033[31mNão há vertice origem\033[m")

    # Funcao para adicionar arestas com origem e destino bem determinados.
    def adiciona_aresta_nao_direcionada(self, vertice_origem, vertice_destino, peso):
        # Caso ja exista o vertice esta conexao sera feita ao fim da lista.
        if vertice_origem in self.grafo:
            if vertice_destino in self.grafo:
                self.grafo[vertice_origem]["arestas"].update(
                    {vertice_destino: peso})
                self.grafo[vertice_destino]["arestas"].update(
                    {vertice_origem: peso})
            else:
                print("\033[31mNão há vertice destino\033[m")

        # Caso ainda nao exista esse vertice se inicia uma lista apenas com seu valor.
        else:
            print("\033[31mNão há vertice origem\033[m")

    # Funcao para remover arestas entre dois vertices.
    def elimina_aresta(self, vertice_origem, vertice_destino):
        # Caso exista a conexao entre os vertices dados e removido o destino da lista de conexoes do dicionario.
        if vertice_origem in self.grafo:
            try:
                del self.grafo[vertice_origem]["arestas"][vertice_destino]
                del self.grafo[vertice_destino]["arestas"][vertice_origem]
            except:
                print("Nao existe conexao de",vertice_origem, "a", vertice_destino)

    # Funcao necessaria para a remocao de vertices.
    def elimina_vertice(self, vertice):
        # Caso exista ele sera removido.
        if vertice in self.grafo:
            # Percorre-se todo o grafo buscando o vertice a ser removido.
            for key in self.grafo:
                # Para o caso de mais uma conexao ao mesmo vertice se removem todas as conexoes ate nao existir mais conexao determinada
                while vertice in self.grafo[key]["arestas"]:
                    print(vertice)
                    self.elimina_aresta(key, vertice)
            del self.grafo[vertice]

    def distancia_de_vertices(self, a, b):
        return round(((self.grafo[a]["coordenadas"]["X"] - self.grafo[b]["coordenadas"]["X"])**2 + (self.grafo[a]["coordenadas"]["Y"] - self.grafo[b]["coordenadas"]["Y"])**2)**1/2,2)

    def cria_grafo_aleatorio(self, numero_de_vertices):
        # Cria e adiciona todos os vertices com os valores de x e y já definidos
        for i in range(numero_de_vertices):
            self.adiciona_vertice_vazio(i, round(random.random(), 2), round(random.random(), 2))
        # Adiciona as arestas entre os vertices, os vizinhos de cada vertice sao apenas os K pontos mais proximos, onde K = parte inteira de log2(n)
        for keys in self.grafo:
            for nearest_key in self.checa_distancias(keys,numero_de_vertices):
                self.adiciona_aresta_nao_direcionada(keys,nearest_key,self.distancia_de_vertices(keys,nearest_key))

    def checa_distancias(self, vertice, numero_de_vertices):
        vertices_mais_proximos = []

        k = math.floor(math.log(numero_de_vertices,2))
        print(k)
        for i in range(k):
            print(vertices_mais_proximos)
            vertices_mais_proximos.append(0)
            aux = 99
            for key in self.grafo:
                if key in vertices_mais_proximos or key == vertice:
                    pass
                else:
                    if aux > self.distancia_de_vertices(vertice,key):
                        print(len(self.grafo[vertice]["arestas"].keys()))
                        if len(self.grafo[vertice]["arestas"].keys()) < k: 
                            aux = self.distancia_de_vertices(vertice,key)
                            vertices_mais_proximos[i] = key
        
        return vertices_mais_proximos