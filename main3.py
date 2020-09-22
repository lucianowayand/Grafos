from leitor_de_entrada import le_entrada
import grafo_lib
import minimo_sucessor
from tkinter import *
from PIL import Image, ImageTk

g = minimo_sucessor.Grafo()

g.grafo_noia()

g.cria_graphviz_tb2()

g.minimos_sucessores()