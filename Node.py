class Node():
    def __init__(self, pai, tabuleiro):
        self.filhoCima = None
        self.filhoDireita = None
        self.filhoBaixo = None
        self.filhoEsquerda = None
        self.pai = pai
        self.listBoolFilhos = [True,True,True,True]
        self.tabuleiro = tabuleiro
    def getBoolFilhos(self):
        return self.listBoolFilhos
    def setBoolFilhos(self, id):
        self.listBoolFilhos[id] = False
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
