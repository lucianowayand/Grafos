from leitor_de_entrada import le_entrada
from grafo_lib import Grafo
from tkinter import *
from PIL import Image, ImageTk


def destroy():  # Mata a primeira tela e armazena o valor da entry caso ela seja válida
    try:
        global num_vertices
        num_vertices = int(vertices.get())
        seletor.destroy()
    except:
        print("Valor inválido")


# Configura a janela para aparecer no centro e não ser re-escalavel
seletor = Tk()
seletor.resizable(height=FALSE, width=FALSE)
seletor.geometry("400x250")
seletor.eval('tk::PlaceWindow %s center' %
             seletor.winfo_pathname(seletor.winfo_id()))
seletor.title("Seletor de tamanho")

# Insere os widgets
info = Label(text="Insira o número de vértices")
info.place(x=110, y=50)

vertices = Entry()
vertices.place(x=110, y=100)

ok = Button(command=destroy, text="Criar")
ok.place(x=160, y=140)

disclaimer = Label(text="Esse processo pode demorar um pouco")
disclaimer.place(x=75, y=200)

# Fim do seletor
seletor.mainloop()


# Janela de exposição de resultado
grafo = Tk()
grafo.title("Grafo resultante de BFS")
grafo.resizable(height=FALSE, width=FALSE)

# Cria um grafo aleatorio e o categoriza de acordo com o BFS
g = Grafo()
g.adiciona_vertice(1)
g.adiciona_vertice(2)
g.adiciona_vertice(3)
g.adiciona_vertice(4)
g.adiciona_vertice(5)
g.adiciona_aresta_nao_direcionada_dic(1, 5, 1)
g.adiciona_aresta_nao_direcionada_dic(1, 2, 1)
g.adiciona_aresta_nao_direcionada_dic(1, 3, 5)
g.adiciona_aresta_nao_direcionada_dic(1, 4, 2)
g.adiciona_aresta_nao_direcionada_dic(2, 3, 1)
g.adiciona_aresta_nao_direcionada_dic(2, 4, 2)
g.adiciona_aresta_nao_direcionada_dic(2, 5, 3)
g.adiciona_aresta_nao_direcionada_dic(3, 4, 1)
g.adiciona_aresta_nao_direcionada_dic(3, 5, 1)
g.adiciona_aresta_nao_direcionada_dic(4, 5, 2)

g.cria_graphviz_tb2()

# Coloca a imagem gerada em uma janela da biblioteca tkinter
img = ImageTk.PhotoImage(Image.open(
    "test-output/grafo.png").resize((800, 800)))
panel = Label(grafo, image=img)
panel.pack()

grafo.mainloop()
