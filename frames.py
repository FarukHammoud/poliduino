
from index import *

#Frames do Programa
                      
class FrameCliente:
    
    #Objetos do Frame
  
    #Variaveis do Frame
    vetor_mouse_em_cima = [False,False,False,False,False,False]
    vetor_pressionado = [False,False,False,False,False,False]
    expansao = 0
    expandido = False
    slots = 4
    expansao_meta = 0
    flag = False
    n_flag = False #reciclavel
    logado = False
    text_box_1 = TextBox(0,0)
    text_box_2 = TextBox(0,0)
    lista_lateral_1 = ListaLateral(0,0)
    lista_lateral_2 = ListaLateral(0,0)
    lista_lateral_3 = ListaLateral(0,0)
    botao_poli = Botao('poli',55,5,'Clique para expandir','Expandir/Contrair')
    botao_entradas = Botao('menu_superior',int(height/6) + int(height/8) + 65,5,'Clique para abrir a leitura de dados','Abrir leitura de dados')
    botao_saidas = Botao('menu_superior',int(height/6) + 2*int((height/8))+ 65,5,'Clique para abrir o controle de portas','Abrir controle de portas')
    botao_arquivo = Botao('menu_superior',int(height/6) + 3*int((height/8))+ 65,5,'Clique para abrir o gerenciador de arquivos','Abrir gerenciador de arquivos')
    botao_add = Botao('menu_superior',int(height/6) + 4*int((height/8))+ 65,5,'Clique para adicionar Plug-in','Abrir adicionar Plug-in')
    botao_poli.MudaTamanho(width/6,height/8-10)
    botao_entradas.MudaTamanho(height/8-10,height/8-10)
    botao_saidas.MudaTamanho(height/8-10,height/8-10)
    botao_arquivo.MudaTamanho(height/8-10,height/8-10)
    botao_add.MudaTamanho(height/8-10,height/8-10)
    botao_concluir = Botao('habilitavel',0,0,'','Estado +=1')
    estado = 0
    one_time = True
    carregador = AnimacaoDeEspera(width/2+390,height/2+145)
    NeivaToolbox = Toolbox('neiva.png')
    Janelas = GerenciadorJanelas()
    #Funcoes do Frame
    def EstadoAdd(self): 
        FrameCliente.estado+=1
    def IniciaImagens(self):
        FrameCliente.foto_usp = loadImage('usp.jpg')
        FrameCliente.poli = loadImage('poli.png')
        FrameCliente.logo_poli = loadImage('poli_logo.png')
        FrameCliente.upload = loadImage('upload.png')
        FrameCliente.download = loadImage('download.png')
        FrameCliente.adicionar = loadImage('add.png')
        FrameCliente.arquivo = loadImage('arquivo.png')
    def ExpandirContrair(self):
        if FrameCliente.expandido: FrameCliente.expansao_meta = 0
        else: FrameCliente.expansao_meta = FrameCliente.slots
    def Animacoes(self):
        if FrameCliente.expansao_meta < FrameCliente.expansao: FrameCliente.expansao -= 1
        elif FrameCliente.expansao_meta > FrameCliente.expansao: FrameCliente.expansao += 1
        FrameCliente.expandido = False
        if FrameCliente.expansao_meta == FrameCliente.expansao: 
            if FrameCliente.expansao == FrameCliente.slots: FrameCliente.expandido = True
    def DesenhaLayout(self):
        noStroke()
        tint(50,50,250)
        image(FrameCliente.foto_usp,0,0,width,height)
        noTint()
        fill(255,255,255,150)
        rect(50,-20,width/6+10+FrameCliente.expansao*(height/8),height/8+20,20)
        FrameCliente.botao_poli.Mostrar()
        image(FrameCliente.logo_poli,60,10,width/6,height/10)
        if FrameCliente.expandido:
            FrameCliente.botao_saidas.Mostrar()
            FrameCliente.botao_entradas.Mostrar()
            FrameCliente.botao_arquivo.Mostrar()
            FrameCliente.botao_add.Mostrar()
            image(FrameCliente.upload,int(height/6) + int(height/8) + 70,10,height/10,height/10)
            image(FrameCliente.download,int(height/6) + 2*int(height/8) + 70 ,10,height/10,height/10)
            image(FrameCliente.arquivo,int(height/6) + 3*int(height/8) + 70,10,height/10,height/10)
            image(FrameCliente.adicionar,int(height/6) + 4*int(height/8) + 70,10,height/10,height/10)
    
    def IniciaObjetos(self):
        #inicializacao das imagens
        if FrameCliente.one_time:
            FrameCliente().IniciaImagens()
            FrameCliente.one_time = False
    def MostraTmpText(self):
        if millis() - Interface().RetornaTempoUltimaTecla() < 2000:
            fill(Cores().amarelo,(2000 - (millis() - Interface().RetornaTempoUltimaTecla()))/3)
            textSize(20)
            text('>'+Interface().RetornaString(),30,height-10)    
  #Visualizacao
    def Mostrar(self): 
        FrameCliente().IniciaObjetos()   
        FrameCliente().DesenhaLayout()
        FrameCliente().Animacoes()
        FrameCliente().Janelas.Mostrar()   
        FrameCliente().NeivaToolbox.Mostrar()  
        FrameCliente().MostraTmpText() 
        textSize(25)
        fill(0)
class FrameAnimacaoInicial:
  
  #Objetos do Frame
  one_time = True   
  tempo_inicial = 0
  #Funcoes do Frame
  def __init__(self):
      pass
    #Variaveis do Frame
    
  def IniciaImagens(self):
      #mus_ini = soundfile()
      #mus_ini = SoundFile(self,"Muse - Undisclosed Desires.mp3")
      #mus_ini.play()
      FrameAnimacaoInicial.foto_usp = loadImage('usp.jpg')
      FrameAnimacaoInicial.logo_poli = loadImage('poli.png')
  #Visualizacao
  def Mostrar(self):
      #inicializacao das imagens
      if FrameAnimacaoInicial.one_time:
        FrameAnimacaoInicial().IniciaImagens()
        FrameAnimacaoInicial.tempo_inicial = millis()
        FrameAnimacaoInicial.one_time = False
      background(255,255,255)
      tint(50,50,250,(millis()-FrameAnimacaoInicial.tempo_inicial)/25)
      image(FrameAnimacaoInicial.foto_usp,0,0,width,height)
      noTint()
      image(FrameAnimacaoInicial.logo_poli,width/2-300,(height-50)/2-100,600,200)  
      #animacao fechamento
      if (millis()-FrameAnimacaoInicial.tempo_inicial) > width*5 :
         par = ((millis()-FrameAnimacaoInicial.tempo_inicial)-width*5)/10 
         if par > 200:
             par = 200
             Tarefas().Tarefa('Desativa Frame Animacao Inicial')
             Tarefas().Tarefa('Ativa Frame Cliente')
      #barra de carregamento
      fill(25,25,100,(millis()-FrameAnimacaoInicial.tempo_inicial)/25)
      noStroke()
      rect(0,height-50,(millis()-FrameAnimacaoInicial.tempo_inicial)/5,5)

class Frames:

  #Lista de Controle
  frame = []

  #Declaracao de Frames
  frame_animacao_inicial = FrameAnimacaoInicial()
  frame_cliente = FrameCliente()
  
  #Metodos
  def __init__(self):
    for i in range(0,20):
      Frames.frame.append(False)
  def AtivaFrame(self,numero): Frames.frame[numero] = True 
  def AtivaFrames(self,lista): 
    for i in lista:
        Frames.frame[i] = True 
  def DesativaFrame(self,numero): Frames.frame[numero] = False
  def DesativaFrames(self,lista): 
    for i in lista:
        Frames.frame[i] = False
  def EstadoFrame(self,numero): return Frames.frame[numero]
  def MouseDentro(self,frame):
      if frame == 0 and Frames().EstadoFrame(0): return True
      elif frame == 1 and Frames().EstadoFrame(1) and Calculo().MouseIn(width/2-440,(height-50)/2-220,880,440): return True
      
  #Funcao Visualizacao
  def Mostrar(self):
    background(0,0,0)
    if Frames.frame[0]: Frames.frame_animacao_inicial.Mostrar()
    if Frames.frame[1]: Frames.frame_cliente.Mostrar()
    if Frames.frame[2]: Frames.frame_servidor.Mostrar()
      