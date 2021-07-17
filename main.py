
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

def verificaMovimento(tabuleiroAtual, no):
    i, j = buscaVazio(tabuleiroAtual)
    tab = copy.deepcopy(tabuleiroAtual)
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
            return noAux

    #Direita
    if(-1 < j - 1 and check == False and no.getfilhoDireita() == None):
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
            return noAux
    # Baixo
    if(-1 < i - 1 and check == False and no.getfilhoBaixo() == None):
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
            return noAux

    # Esquerda
    if(n > j + 1 and check == False and no.getfilhoEsquerda() == None):
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
            return noAux

    return no.getPai()


 
def backTracking (tabuleiroInicial, tabuleiroFinal):
    raiz = Node(None, copy.deepcopy(tabuleiroInicial))
    no = raiz
    sucesso = verificaObjetivo(no.getTab(), tabuleiroFinal)
    fracasso = False
    while (sucesso == False and fracasso == False):
        no = verificaMovimento(no.getTab(), no)
        if(no == None):
            fracasso = True
        else:
            sucesso = verificaObjetivo(no.getTab(), tabuleiroFinal)
        # print(no.getTab())
    print(sucesso)
    print(fracasso)

def getInvCount(arr):
    inv_count = 0
    i=0
    for i in range(9 -1):
        j = i + 1
        for j in range(9):
             if (arr[j] and arr[i] and arr[i] > arr[j]):
                  inv_count += 1
    return inv_count

def isSolvable(puzzle):
    invCount = getInvCount(int(puzzle))
 
    return (invCount%2 == 0)

def main():
    global n
    tabuleiroInicial = []
    tabuleiroFinal = []
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