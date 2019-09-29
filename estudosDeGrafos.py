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
    def addAresta(self, vertice1, vertice2, valor):         #Adicionando arestas com o método update ele é capaz de adicionar dicionários até mesmo a dicionários já existentes              
            self.grafo[vertice1].update({vertice2:valor})             
            self.grafo[vertice2].update({vertice1:valor})
