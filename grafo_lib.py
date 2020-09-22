# numpy serve para criação de matrizes, será utilizada principalmente no algoritmo de ordenação de arestas por peso
from tkinter.constants import FALSE
import numpy as np

# defaultdict e uma funcao importante para o inicio de um dicionario vazio.
from collections import defaultdict

# As bibliotecas random e math, são utilizadas no posicionamento e calculo de K(log)
import random
import math

# Graphviz e utilizado para formar a representação gráfica abaixo se configura o grafo a ser representado
# de modo a determinar o formato, sua construção e método de inserção.
from graphviz import Graph
dot = Graph('Grafo', format='png', engine='sfdp', strict=True)

color_list = ['pink', 'magenta', 'indigo', 'blue', 'lightseagreen', 'green', 'yellowgreen',
              'yellow', 'goldenrod', 'orange', 'orangered', 'red', 'rosybrown1', 'white', 'grey', 'black']


class Grafo():
    # Funcao construtora que pode ou nao receber o grafo pre determinado.
    def __init__(self, grafo=defaultdict(dict)):
        # Caso não receba um grafo se inicia um dicionario vazio, caso contrario se insere o valor recebido.
        self.grafo = grafo
        self.numero_de_vertices = 0

    def adiciona_vertice(self, vertice):
        # Adiciona um vertice sem as informações de coordenadas.
        self.grafo[vertice] = {'arestas': {}}
        self.grafo[vertice]['japassei'] = 0
        self.numero_de_vertices += 1
    # Funcao para adicionar arestas com origem e destino bem determinados.
    def adiciona_aresta_nao_direcionada_dic(self, vertice_origem, vertice_destino, peso):
        if vertice_origem in self.grafo:
            if vertice_destino in self.grafo:
                self.grafo[vertice_origem]["arestas"].update(
                    {vertice_destino: {'peso': peso}})
                self.grafo[vertice_destino]["arestas"].update(
                    {vertice_origem: {'peso': peso}})
            else:
                print("\033[31mNão há vertice destino\033[m")
        else:
            print("\033[31mNão há vertice origem\033[m")

    def adiciona_aresta_direcionada(self, vertice_origem, vertice_destino, peso):
        # Checa a existencia dos vertices antes de conecta-los.
        if vertice_origem in self.grafo:
            if vertice_destino in self.grafo:
                self.grafo["arestas"].update({vertice_destino: peso})
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
                print("Nao existe conexao de",
                      vertice_origem, "a", vertice_destino)

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

    # Esta funcao adiciona vertices vazios.
    def adiciona_vertice_vazio(self, vertice, x, y):
        # Caso nao exista o vertice ele sera iniciado com uma lista vazia ou reinicia as informações de um vertice existente.
        self.grafo[vertice] = {'coordenadas': {'X': x, 'Y': y}, 'arestas': {}}

    def cria_grafo_aleatorio(self, numero_de_vertices):
        # Cria e adiciona todos os vertices com os valores de x e y já definidos
        for i in range(numero_de_vertices):
            self.adiciona_vertice_vazio(
                i, round(random.random(), 4), round(random.random(), 4))

        # Adiciona as arestas entre os vertices, os vizinhos de cada vertice sao apenas os K pontos mais proximos, onde K = parte inteira de log2(n)
        k = math.floor(math.log(numero_de_vertices, 2))

        for vertices in self.grafo:

            vertices_mais_proximos = []

            for i in range(k):  # Insere k vertices em sua lista de vizinhos
                # Embromation para solucionar o erro de array out of index
                vertices_mais_proximos.append(0)
                aux = 99  # Numero representativo maior que 1.

                for __vertices in self.grafo:  # Verifica para todos os vertices no grafo:
                    # Se ja fazem parte da lista de vertices proximos, pulando o caso de si mesmo.
                    if __vertices in vertices_mais_proximos or __vertices == vertices:
                        pass

                    else:  # Ou se a distancia do vertice é inferior ao menor que havia encontrado, excluso os casos acima descritos.
                        if aux > self.distancia_de_vertices(vertices, __vertices):
                            aux = self.distancia_de_vertices(
                                vertices, __vertices)
                            vertices_mais_proximos[i] = __vertices

            # Adiciona-se aresta entre os vertices mais proximos e o vertice, com peso determinado pela distancia.
            for vertices_proximos in vertices_mais_proximos:
                self.adiciona_aresta_nao_direcionada_dic(
                    vertices, vertices_proximos, self.distancia_de_vertices(vertices, vertices_proximos))

    def cria_graphviz(self):
        for vertice1 in self.grafo:  # Percorre o grafo incluindo os vertices
            dot.node(str(vertice1))
            for vertice2 in self.grafo[vertice1]['arestas']:
                # Preparacao para printar só a aresta de ida e nao a de volta
                self.grafo[vertice1]['arestas'][vertice2]['jaPassei'] = 0
        for vertice1 in self.grafo:  # Depois conecta os vertices com as arestas determinadas
            for vertice2 in self.grafo[vertice1]['arestas']:
                if self.grafo[vertice1]['arestas'][vertice2]['jaPassei'] == 0:
                    self.grafo[vertice1]['arestas'][vertice2]['jaPassei'] = 1
                    self.grafo[vertice2]['arestas'][vertice1]['jaPassei'] = 1
                    dot.edge(str(vertice1), str(vertice2), label=str(
                        self.grafo[vertice1]['arestas'][vertice2]['peso']))


    def ord_pesos_das_arestas(self):
        print(self.grafo)
        lista = []
        for vertice1 in self.grafo:
            for vertice2 in self.grafo[vertice1]['arestas']:
                jaExiste = False
                for tupla in lista:
                    # Verifico se já existe a aresta na lista para nao adicionar duplicados.
                    if(vertice2 == tupla[0] and vertice1 == tupla[1]):
                        jaExiste = True
                if(not jaExiste):
                    # para percorrer a lista e a tupla para acessar o peso = lista[linha][coluna].
                    lista.append(
                        (vertice1, vertice2, self.grafo[vertice1]['arestas'][vertice2]['peso']))
        ordenados = sorted(lista, key=lambda peso: peso[2])
        print(ordenados)

        # Tá agora tenho que ir pegando as arestas em coloca-las em ordem de menor a maior e controlar que não fechem ciclo nem tenham grau maior a 2.
        # criar um novo grafo para nao mexer com o principal, logo ir adicionando nesse grafo vazio as arestas um por um,
        # cada vez que adiciono uma nova aresta controlo se o grafo possui ciclos, se não continuo com o processo. Logo deveria finalizar com um ciclo na ultima aresta :)
