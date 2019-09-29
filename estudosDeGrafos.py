from collections import defaultdict
import os
os.system("cls")

"""
Notas:

- g.grafo[verticeOrigem].get(verticeDestino) // Retorna o valor de um peso

"""

class Grafo:
    def __init__(self ,vertices):
        self.numeroDeVertices = vertices
        self.grafo = defaultdict(dict) 

    #Adiciona Aresta
    def addAresta(self, vertice1, vertice2, valor):                     
        if vertice1 not in self.grafo.keys():                           #Se não encontrar o vertice na lista de vertices do grafo, adicione um dicionario
            self.grafo[vertice1]={vertice2:valor}
        else:                                                           #Encontrando, adicione o novo valor ao dicionario existente
            self.grafo[vertice1].update({vertice2:valor})               
       
        if vertice2 not in self.grafo.keys():
            self.grafo[vertice2]={vertice1:valor}
        else:
            self.grafo[vertice2].update({vertice1:valor})