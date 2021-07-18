
import copy

n = 3

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

# ordem Backtracking:
# Cima 
# Direita
# Baixo
# Esquerda

def imprimeArvore(no,nivel):
    global n
    if (no != None):
        print("Nível: " + str(nivel))
        for i in range(n):
            print(no.getTab()[i])
        print('Cima')
        imprimeArvore(no.getfilhoCima(), nivel+1)
        print('Direita')
        imprimeArvore(no.getfilhoDireita(), nivel+1)
        print('Baixo')
        imprimeArvore(no.getfilhoBaixo(), nivel+1)
        print('Esquerda') 
        imprimeArvore(no.getfilhoEsquerda(), nivel+1)

def buscaVazio(tabuleiroAtual):
    global n
    for i in range (n):
        for j in range (n):
            if tabuleiroAtual[i][j] == '-':
                return i,j

def verificaObjetivo(tabuleiroAtual, tabuleiroFinal):
    if tabuleiroAtual != tabuleiroFinal: 
        return False
    return True

def verificalistaBacktracking(no) :
    global n
    noAux = no.getPai()
    boolean = False
    while(noAux != None):
        if noAux.getTab() == no.getTab():
            return False
        noAux = noAux.getPai()
    return True

def verificaCima(no):
    i, j = buscaVazio(no.getTab())
    tab = copy.deepcopy(no.getTab())
    global n
    check = False
    if(n > i + 1 and no.getfilhoCima() == None):
        tab[i][j] = tab[i+1][j]
        tab[i+1][j] = '-'
        aux = copy.deepcopy(tab)
        noAux = Node(no, aux)
        check = verificalistaBacktracking(noAux)
        if check == False:
            tab[i+1][j] = tab[i][j]
            tab[i][j] = '-'
        if check == True:
            no.setfilhoCima(noAux)
            return noAux, check
    return no, check

def verificaDireita( no):
    i, j = buscaVazio(no.getTab())
    tab = copy.deepcopy(no.getTab())
    global n
    check = False
    if(-1 < j - 1 and no.getfilhoDireita() == None):
        tab[i][j] = tab[i][j-1]
        tab[i][j-1] = '-'
        aux = copy.deepcopy(tab)
        noAux = Node(no, aux)
        check = verificalistaBacktracking(noAux)
        if check == False:
            tab[i][j-1] = tab[i][j]
            tab[i][j] = '-'
        if check == True:
            no.setfilhoDireita(noAux)
            return noAux, check

    return no, check

def verificaBaixo(no):
    i, j = buscaVazio(no.getTab())
    tab = copy.deepcopy(no.getTab())
    global n
    check = False
    if(-1 < i - 1 and no.getfilhoBaixo() == None):
        tab[i][j] = tab[i-1][j]
        tab[i-1][j] = '-'
        aux = copy.deepcopy(tab)
        noAux = Node(no, aux)
        check = verificalistaBacktracking(noAux)
        if check == False:
            tab[i-1][j] = tab[i][j]
            tab[i][j] = '-'
        if check == True:
            no.setfilhoBaixo(noAux)  
            return noAux, check
    
    return no, check

def verificaEsquerda(no):
    i, j = buscaVazio(no.getTab())
    tab = copy.deepcopy(no.getTab())
    global n
    check = False
    if(n > j + 1 and no.getfilhoEsquerda() == None):
        tab[i][j] = tab[i][j+1]
        tab[i][j+1] = '-'
        aux = copy.deepcopy(tab)
        noAux = Node(no, aux)
        check  = verificalistaBacktracking(noAux)
        if check == False:
            tab[i][j+1] = tab[i][j]
            tab[i][j] = '-'
        if check == True:
            no.setfilhoEsquerda(noAux)
            return noAux, check 

    return no, check

def backTracking (tabuleiroInicial, tabuleiroFinal):
    raiz = Node(None, copy.deepcopy(tabuleiroInicial))
    no = raiz
    sucesso = verificaObjetivo(no.getTab(), tabuleiroFinal)
    fracasso = False
    check = False
    while (sucesso == False and fracasso == False):

        no, check = verificaCima(no)
        if check == False:
            no, check = verificaDireita(no)
        if check == False:
            no, check = verificaBaixo(no)
        if check == False:
            no, check = verificaEsquerda(no)
        if check == True:
            sucesso = verificaObjetivo(no.getTab(),tabuleiroFinal)

        elif check == False:
            no = no.getPai()
            if no == None:
                fracasso = True
        # print(no.getTab())
    print(sucesso)
    print(fracasso)

def main():
    global n
    tabuleiroInicial = []
    tabuleiroFinal = []
    print("Digite o estado Inicial da tabela")
    for i in range (n):
        tabuleiroInicial.append([])
        for j in range (n):
            tabuleiroInicial[i].append(input())

    print("Digite o estado final da tabela")
    for i in range (n):
        tabuleiroFinal.append([])
        for j in range (n):
            tabuleiroFinal[i].append(input())
    # for i in range (3):
    #     for j in range (3):
    #         print(tabuleiroInicial[i][j])
    # for i in range (3):
    #     for j in range (3):
    #         print(tabuleiroFinal[i][j])

    backTracking(tabuleiroInicial, tabuleiroFinal)

main()