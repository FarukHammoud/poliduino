#-------------------------------------------------------------------------------#
# Ola,                                                                          #
# Eu sou Faruk, e esse eh o codigo do Poliduino                                 #
# Um software feito para ser uma interface entre o arduino e o usuario          #
#                                                                               #
#-------------------------------------------------------------------------------#
# Versao: 0.1 (20/05/2017) . Por Faruk Hammoud, 2017.                           #
# Compilado em Processing 3.3.3 (by Processing Foundation) - Python Mode        #
# Distribuicao Livre                                                            #
# Suporte 24/7 : farukhammoud@gmail.com                                         #
#-------------------------------------------------------------------------------#
#Importa bibliotecas 
#Importa demais modulos do programa
from index import *
from interface import *

def stop():
    Interface().MudaString('Salvando dados ...')
    Frames().Mostrar()
    Data().SalvaDadosDeComunicacao()
def setup():
    fullScreen()
    frameRate(20)
    
    Tarefas().Tarefa('Ativa Frame Animacao Inicial')
    #Tarefas().Tarefa('Pula Inicio')
    Tarefas().AlteraTarefaLetra('Pula Inicio',' ')
    Tarefas().AlteraTarefaCodigo('Processa Scroll Up','SCROLLUP')
    Tarefas().AlteraTarefaCodigo('Processa Scroll Down','SCROLLDOWN')
    Tarefas().AlteraTarefaCodigo('Estabelece Referencia','MOUSEPRESSED')
    Tarefas().AlteraTarefaCodigo('Calcula Arraste Mouse','MOUSEDRAGGED')
    Tarefas().AlteraTarefaCodigo('Calcula Referencia','MOUSERELEASED')

def draw():
    Frames().Mostrar()
       