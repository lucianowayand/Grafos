from leitor_de_entrada import le_entrada
from grafo_lib import Grafo


g = Grafo()
print('\nESCOLHA UMA DAS OPCOES:')
print('GRAFO DE:')
print('1- 50 vertices')
print('2- 100 vertices')
print('3- 200 vertices')
print('4- 300 vertices')
entrada = int(input())
if(entrada == 1):
    g.cria_grafo_aleatorio(50)
elif(entrada == 2):
    g.cria_grafo_aleatorio(100)
elif(entrada == 3):
    g.cria_grafo_aleatorio(200)
elif(entrada == 4):
    g.cria_grafo_aleatorio(300)
print("Criando grafo, espere por favor...")
g.cria_graphviz()
print("\nGRAFO CRIADO COM SUCESSO!\n")
print('\nPressione "0" para mostrar o BFS...')
if int(input()) == 0:
    g.iniciarBFS()
    g.cria_graphviz()
