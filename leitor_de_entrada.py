#defaultdict e uma funcao importante para o inicio de um dicionario vazio.
from collections import defaultdict

#Leitura de arquivo com selecao de arquivo bem determinada.
def le_entrada(path=r"C:\Users\Luciano\Code\Python\Grafos\entrada.txt"):
    input_file = open(path,"r") 
    #Separacao de linhas
    f_text = input_file.read().split("\n")

    #Separacao de valores.
    aux = []
    for lines in f_text:
        #Utiliza-se o .replace para remover o ":" que aparece ao lado da entrada padrao.
        aux.append(lines.replace(":","").split(" "))

    #Transcricao dos valores obtidos na entrada para o metodo de trabalho escolhido, em dicionario.
    grafo = defaultdict(dict)
    #Ele percorrera toda a lista e iniciara os marcadores do dicionario como listas vazias.
    for keys in range(len(aux)):
        grafo[aux[keys][0]] = []
        #Agora ele adicionara as listas os valores que acompanham.
        for values in range(1,len(aux[keys])):
            grafo[aux[keys][0]].append(aux[keys][values])

    #Retorna o grafo obtido apos o tratamento.
    return grafo
