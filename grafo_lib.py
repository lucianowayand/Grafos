#defaultdict e uma funcao importante para o inicio de um dicionario vazio.
from collections import defaultdict

class Grafo():
    #Funcao construtora que pode ou nao receber o grafo pre determinado, o ideal e utilizar a funcao le_entrada para o tal.
    def __init__(self,grafo):
        #Caso não receba um grafo se inicia um dicionario vazio.
        if grafo == None:
            self.grafo = defaultdict(dict)
        self.grafo = grafo

    #Esta funcao adiciona vertices vazios.
    def adiciona_vertice(self, vertice):
        #Caso nao exista o vertice ele sera iniciado com uma lista vazia.
        if vertice not in self.grafo:
            self.grafo[vertice]=[]

    #Funcao necessaria para a remocao de vertices.
    def elimina_vertice(self, vertice):
        #Caso exista ele sera removido.
        if vertice in self.grafo:
            del self.grafo[vertice]
    
    #Funcao para adicionar arestas com origem e destino bem determinados.
    def adiciona_aresta_direcionada(self,vertice_origem,vertice_destino):
        #Caso ja exista o vertice esta conexao sera feita ao fim da lista.
        if vertice_origem in self.grafo:
            self.grafo[vertice_origem].append(vertice_destino)
        #Caso ainda nao exista esse vertice se inicia uma lista apenas com seu valor.
        else:
            self.grafo[vertice_origem] = [vertice_destino]

    #Funcao para remover arestas entre dois vertices.
    def elimina_aresta(self,vertice_origem,vertice_destino):
        #Caso exista a conexao entre os vertices dados e removido o destino da lista de conexoes do dicionario.
        if vertice_origem in self.grafo:
            try:
                self.grafo[vertice_origem].remove(vertice_destino)
            except:
                print("Nao existe conexao de",vertice_origem,"a",vertice_destino)