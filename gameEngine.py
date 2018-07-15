# Import a library of functions called 'pygame'
import pygame
from math import pi

# define algumas tuplas para serem usads

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)


class Teclado():
    """
    pega o valor do teclado
    """
    def __init__(self):
        self.event=None
        self.tecla =""

    def setEvent(self,event):
        if(event is not None):
            if event.type == pygame.KEYDOWN:
                self.tecla = event.unicode
                # a
            if event.type == pygame.KEYUP:
                # 97
                self.tecla = str(event.key)

            print(self.tecla)

    def getButton(self):
        if(self.event is not None):
            return self.tecla
        return None


class Mouse():
    """
    pega o valor do mouse
    """
    def __init__(self):

        self.event=None
        self.botao =-1
        self.pos =()

    def setEvent(self,event):
        if(event is not None):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.event=event
                self.botao = event.button
                self.pos = event.pos
            if event.type == pygame.MOUSEMOTION:
                self.botao = -1
                self.pos = event.pos

            print('button {} pressed in the position {}'.format(self.botao, self.pos))

    def getPos(self):
        if(self.event is not None):
            return self.event.position
        return None

    def getButton(self):
        if(self.event is not None):
            return self.event.button
        return None

class Jogo():
    """
    Classe que elimina o boilerplate code para facilitar o uso do pygame
    """
    def __init__(self, tamanhoTela=[400, 300],taxaAtual = 10):
        # jogo
        pygame.init()
        self.__done = False
        self.__taxaAtua = taxaAtual
        self.clock = pygame.time.Clock()

        # informacaoes da tela
        self.size = tamanhoTela
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Game")

        # teclado
        self.teclado = Teclado()


        # mouse
        self.mouse = Mouse()



    def getScreen(self):
        return self.screen


    def configura(self):
        """
        funcao que deve ser implementada na classe filha para configurar o jogo
        """
        pass


    def logica(self):
        """
        essa é o meotodo que o programador deve implementar a logica do jogo
        """
        pass

    def eventos(self):
        pass
        # pygame.draw.rect(self.screen, BLACK, [150, 10, 50, 20])

    def __endGame(self,event):
        """
        metodo para terminar o jogo
        """
        if event.type == pygame.QUIT: # If user clicked close
            self.__done = True # Flag that we are done so we exit


    def denhraFundo(self):
        self.screen.fill(WHITE)


    def roda(self):
        while not self.__done:
            for event in pygame.event.get(): # User did something
                self.__endGame(event)
                self.mouse.setEvent(event)
                self.teclado.setEvent(event)


            # define taxa de atualizacao
            self.clock.tick(self.__taxaAtua)
            #por default pinta a tela de branco
            self.denhraFundo()

            # faz a logica apos pintar de branco
            self.logica()
            pygame.display.flip()
        pygame.quit()


class Obj():
    """
    Interface do objeto do jogo
    """
    def desenha(self):
        """
        Funcao que deve ser implementada para desenhar
        """
        pass

    def atualiza(self):
        """
        Funcao que serve para atualizar a lógica do desenho
        """
        pass
