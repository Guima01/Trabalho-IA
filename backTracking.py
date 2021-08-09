from Node import *
import copy
from queue import Queue

n = 0
m = 0
fechados = []
abertos = Queue()

def imprimeArvore(no,nivel):
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
    global m
    for i in range (n):
        for j in range (m):
            if tabuleiroAtual[i][j] == '-':
                return i,j

def verificaObjetivo(tabuleiroAtual, tabuleiroFinal):
    if tabuleiroAtual != tabuleiroFinal: 
        return False
    return True

def verificalistaBacktracking(no) :
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
    global m
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
    global m
    check = False
    if(m > j + 1 and no.getfilhoEsquerda() == None):
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

def backTracking (tabuleiroInicial, tabuleiroFinal, linha, coluna):
    global n
    global m 
    n = linha
    m = coluna   
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