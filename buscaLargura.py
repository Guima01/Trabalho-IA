from Node import *
import copy
from queue import Queue

n = 3
fechados = []

def verificaObjetivo(tabuleiroAtual, tabuleiroFinal):
    if tabuleiroAtual != tabuleiroFinal: 
        return False
    return True

def buscaVazio(tabuleiroAtual):
    global n
    for i in range (n):
        for j in range (n):
            if tabuleiroAtual[i][j] == '-':
                return i,j

def verificaRepeticao(no) :
    global n
    global fechados
    for node in fechados:
        if node.getTab() == no.getTab():
            return False
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
        check = verificaRepeticao(noAux)
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
        check = verificaRepeticao(noAux)
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
        check = verificaRepeticao(noAux)
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
        check  = verificaRepeticao(noAux)
        if check == False:
            tab[i][j+1] = tab[i][j]
            tab[i][j] = '-'
        if check == True:
            no.setfilhoEsquerda(noAux)
            return noAux, check 

    return no, check

def buscaLargura(tabuleiroInicial, tabuleiroFinal):
    abertos = Queue()
    global fechados
    raiz = Node(None, copy.deepcopy(tabuleiroInicial))
    sucesso = verificaObjetivo(raiz.getTab(), tabuleiroFinal)
    abertos.put(copy.deepcopy(raiz))
    fracasso = False
    check = False
    while(sucesso == False and fracasso == False):
        if abertos.empty():
            fracasso = True
        else:
            no = abertos.get()
            fechados.append(no)
            if verificaObjetivo(no.getTab(),tabuleiroFinal):
                sucesso = True
            else:
                aux, check = verificaCima(no)
                if check == True:
                    # print('cima')
                    abertos.put(copy.deepcopy(aux))
                aux, check = verificaDireita(no)
                if check == True:
                    # print('direita')
                    abertos.put(copy.deepcopy(aux))
                aux, check = verificaBaixo(no)
                if check == True:
                    # print('baixo')
                    abertos.put(copy.deepcopy(aux))
                aux, check = verificaEsquerda(no)
                if check == True:
                    # print('esquerda')
                    abertos.put(copy.deepcopy(aux))

    print(sucesso)
    print(fracasso)