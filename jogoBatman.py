from gameEngine import *



class ObjGame(Obj):
    """
    exemplo de um objeto que pode ser implementado no jogo
    """
    def __init__(self, tela):
        self.screen = tela
        self.width = 50
        self.height = 20
        self.x = 150
        self.y = 10

    def desenha(self):
        pygame.draw.rect(self.screen, BLACK, [self.x, self.y, self.width,self.height])

    def checaBorda(self):
        if self.x < 0 :
            # print("entrou1")
            return True

        if self.x + self.width > self.screen.get_width():
            # print("entrou2")
            return True

        if self.y < 0 :
            # print("entrou2")
            return True


        if (self.y + self.height) > self.screen.get_height():
            # print("entrou3")
            return True


        return False


    def atualiza(self):
        if(not self.checaBorda()):
            self.y = self.y + 5

class ObjGameCriculo(ObjGame):
    def __init__(self, tela):
        super().__init__(tela)

    def desenha(self):
        pygame.draw.ellipse(self.screen, RED, [self.x, self.y, self.width, self.height])

    def atualiza(self):
        if(not self.checaBorda()):
            self.x = self.x + 5

# exemplo de uso da calsse Jogo
class JogoDaVelha(Jogo):
    """
    exemplo de implementação  da classe Jogo
    """
    def __init__(self):
        super().__init__([500,500],10)
        self.p1 = ObjGame(self.getScreen())
        self.p2 = ObjGameCriculo(self.getScreen())

    def denhraFundo(self):
        self.screen.fill(BLUE)

    def logica(self):
        self.p1.desenha()
        self.p2.desenha()
        self.p1.atualiza()
        self.p2.atualiza()



jg = JogoDaVelha()
jg.roda()
