import grafo_lib

class Grafo(grafo_lib.Grafo):
    def busca_em_largura(self, lista_de_vertices, t):
        # Percorre a lista de vértices de modo a abrigar o caso de grafos disconexos.
        while lista_de_vertices != []:
            v = lista_de_vertices[0]
            del lista_de_vertices[0]

            # Percorre todas as conexões com o vertice v
            for w in self.grafo[v]['arestas']:
                if self.grafo[w]['indice'] == 0:
                    self.grafo[w]['pai'] = v
                    self.grafo[w]['nivel'] = self.grafo[v]['nivel'] + 1
                    t += 1
                    self.grafo[w]['indice'] = t
                    lista_de_vertices.append(w)
                # Caso w seja irmão de v ou sobrinho a cor das arestas muda.
                elif self.grafo[w]['nivel'] == self.grafo[v]['nivel']:
                    if self.grafo[w]['pai'] == self.grafo[v]['pai']:
                        dot.edge(str(v), str(w), color='red')
                elif self.grafo[w]['nivel'] == self.grafo[v]['nivel'] + 1:
                    dot.edge(str(v), str(w), color='green')
                # Ao fim pinta-se w de acordo com seu nível.
                dot.node(
                    str(w), fillcolor=color_list[self.grafo[w]['nivel']], style='filled')

    def iniciarBFS(self):  # Funcao de preparação, copia o grafo em um auxiliar de tratamento
        # Inicialização de valores
        t = 0
        f = []
        # Pinta o grafo raiz para mudar as cores a cada interação.
        self.aquarela()

        for vertice in self.grafo:  # Adiciona a cada vertice as chaves de informação necessárias
            self.grafo[vertice]['pai'] = None
            self.grafo[vertice]['indice'] = 0
            self.grafo[vertice]['nivel'] = 0

        for _vertice in self.grafo:  # E altera o indice a cada interação
            t += 1
            self.grafo[_vertice]['indice'] = t
            f.append(_vertice)
            self.busca_em_largura(f, t)

    def aquarela(self):
        dot.node('0', fillcolor=color_list[0], style='filled')
        for vertice1 in self.grafo:
            for vertice2 in self.grafo[vertice1]['arestas']:
                if vertice1 == 0 or vertice2 == 0:
                    pass
                else:
                    dot.edge(str(vertice1), str(vertice2), color='yellow')

    
        # Cria o arquivo do grafo
        dot.render('test-output/grafo')