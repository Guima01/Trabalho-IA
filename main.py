
import copy

n = 2

class Node():
    def __init__(self, pai, tabuleiro):
        self.filhoCima = None
        self.filhoDireita = None
        self.filhoBaixo = None
        self.filhoEsquerda = None
        self.pai = pai
        self.listBoolFilhos = [True,True,True,True]
        self.tabuleiro = tabuleiro
    # def getId(self):
    #     return self.id
    # def getIdPai(self):
    #     return self.idPai
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
    # def getFechado(self):
    #     return self.fechado

# ordem Backtracking:
# Cima 
# Direita
# Baixo
# Esquerda

def imprimeArvore(no):
    global n
    if (no != None):
        for i in range(n):
            print(no.getTab()[i])
        print("cima")
        imprimeArvore(no.getfilhoCima())
        print("direita")
        imprimeArvore(no.getfilhoDireita())
        print("baixo")
        imprimeArvore(no.getfilhoBaixo())
        print("esquerda")
        imprimeArvore(no.getfilhoEsquerda())

def buscaVazio(tabuleiroAtual):
    global n
    for i in range (n):
        for j in range (n):
            if tabuleiroAtual[i][j] == '-':
                print(i)
                print(j)
                for x in range(n):
                    print(tabuleiroAtual[x])
                return i,j

def verificaObjetivo(tabuleiroAtual, tabuleiroFinal):
    if tabuleiroAtual != tabuleiroFinal: 
        return False
    return True

def verificalistaBacktracking(noAtual) :
    global n
    noAux = noAtual.getPai()
    boolean = False
    while(noAux != None):
        if noAux.getTab() == noAtual.getTab():
            return False
        noAux = noAux.getPai()
    return True

def verificaMovimento(tabuleiroAtual, i, j, no):
    global n
    check = False
    checkSide = ''
    #cima
    if(n > i + 1 and no.getfilhoCima() == None):
        tabuleiroAtual[i][j] = tabuleiroAtual[i+1][j]
        tabuleiroAtual[i+1][j] = '-'
        aux = copy.deepcopy(tabuleiroAtual)
        noAux = Node(no, aux)
        check  = verificalistaBacktracking(noAux)
        if check == False:
            tabuleiroAtual[i+1][j] = tabuleiroAtual[i][j]
            tabuleiroAtual[i][j] = '-'
            noAux = Node(no, tabuleiroAtual)
        checkSide = 'cima'
    #Direita
    if(-1 < j - 1 and check == False and no.getfilhoDireita() == None):
        tabuleiroAtual[i][j] = tabuleiroAtual[i][j-1]
        tabuleiroAtual[i][j-1] = '-'
        aux = copy.deepcopy(tabuleiroAtual)
        noAux = Node(no, aux)
        check  = verificalistaBacktracking(noAux)
        if check == False:
            tabuleiroAtual[i][j-1] = tabuleiroAtual[i][j]
            tabuleiroAtual[i][j] = '-'
            noAux = Node(no, aux)
        checkSide = 'direita'
    # Baixo
    if(-1 < i - 1 and check == False and no.getfilhoBaixo() == None):
        tabuleiroAtual[i][j] = tabuleiroAtual[i-1][j]
        tabuleiroAtual[i-1][j] = '-'
        aux = copy.deepcopy(tabuleiroAtual)
        noAux = Node(no, aux)
        check = verificalistaBacktracking(noAux)
        if check == False:
            tabuleiroAtual[i-1][j] = tabuleiroAtual[i][j]
            tabuleiroAtual[i][j] = '-'
        checkSide = 'baixo'    
    # Esquerda
    if(n > j + 1 and check == False and no.getfilhoEsquerda() == None):
        tabuleiroAtual[i][j] = tabuleiroAtual[i][j+1]
        tabuleiroAtual[i][j+1] = '-'
        aux = copy.deepcopy(tabuleiroAtual)
        noAux = Node(no, aux)
        check  = verificalistaBacktracking(noAux)
        if check == False:
            tabuleiroAtual = aux
            noAux = Node(no, aux)
        checkSide = 'esquerda'


    if check == True:
        if checkSide == 'cima':
            no.setfilhoCima(noAux)
        if checkSide == 'direita':
            no.setfilhoDireita(noAux)
        if checkSide == 'baixo':
            no.setfilhoBaixo(noAux)
        if checkSide == 'esquerda':
            no.setfilhoEsquerda(noAux)

    if check == False:
        noAux = no.getPai()
        # print('ENTREI')

    # print(noAux)
    # print(noAux.getPai())
    # print(noAux.getfilhoCima())
    # print(noAux.getfilhoDireita())
    # print(noAux.getfilhoBaixo())
    # print(noAux.getfilhoEsquerda())
    # for i in range(n):
    #         print(no.getTab()[i])
    return noAux
 
def backTracking (tabuleiroInicial, tabuleiroFinal):
    raiz = Node(None, copy.deepcopy(tabuleiroInicial))
    no = raiz
    tabuleiroAtual = copy.deepcopy(tabuleiroInicial)
    sucesso = verificaObjetivo(no.getTab(), tabuleiroFinal)
    fracasso = False
    i = 0
    while (sucesso == False and fracasso == False and i < 14):
        linha, coluna = buscaVazio(tabuleiroAtual)
        no = verificaMovimento(tabuleiroAtual, linha, coluna, no)
        if(no == None):
            fracasso = True
        else:
            sucesso = verificaObjetivo(no.getTab(), tabuleiroFinal)
        i += 1
    # print(sucesso)
    # print(fracasso)
    # imprimeArvore(raiz)

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