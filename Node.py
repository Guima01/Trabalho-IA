class Node():
    def __init__(self, pai, tabuleiro):
        self.filhoCima = None
        self.filhoDireita = None
        self.filhoBaixo = None
        self.filhoEsquerda = None
        self.pai = pai
        self.tabuleiro = tabuleiro
        self.custo = 0
    def setTab(self, tab):
        self.tabuleiro = tab
    def getTab(self):
        return self.tabuleiro
    def getfilhoCima(self):
        return self.filhoCima
    def getfilhoDireita(self):
        return self.filhoDireita
    def getfilhoBaixo(self):
        return self.filhoBaixo    
    def getfilhoEsquerda(self):
        return self.filhoEsquerda
    def setfilhoCima(self, no):
        self.filhoCima = no
    def setfilhoDireita(self, no):
        self.filhoDireita = no
    def setfilhoBaixo(self, no):
        self.filhoBaixo = no
    def setfilhoEsquerda(self, no):
        self.filhoEsquerda = no
    def getPai(self):
        return self.pai
    def setPai(self, no):
        self.pai = no
    def setCusto(self, custo):
        self.custo = custo
    def getCusto(self):
        return self.custo
