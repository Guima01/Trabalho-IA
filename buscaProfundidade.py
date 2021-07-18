from Node import *
import copy
from queue import LifoQueue

import sys
sys.setrecursionlimit(1000000000)


fechados = []
abertos = LifoQueue()
n = 3

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
    global abertos
    global n
    check = False
    if(n > i + 1):
        tab[i][j] = tab[i+1][j]
        tab[i+1][j] = '-'
        aux = copy.deepcopy(tab)
        noAux = Node(no, aux)
        check = verificaRepeticao(noAux)
        if check == False:
            tab[i+1][j] = tab[i][j]
            tab[i][j] = '-'
        if check == True:
            # no.setfilhoCima(noAux)
            abertos.put(noAux)
            return noAux, check
    
    return no, check

def verificaDireita( no):
    i, j = buscaVazio(no.getTab())
    tab = copy.deepcopy(no.getTab())
    global abertos
    global n
    check = False
    if(-1 < j - 1):
        tab[i][j] = tab[i][j-1]
        tab[i][j-1] = '-'
        aux = copy.deepcopy(tab)
        noAux = Node(no, aux)
        check = verificaRepeticao(noAux)
        if check == False:
            tab[i][j-1] = tab[i][j]
            tab[i][j] = '-'
        if check == True:
            # no.setfilhoDireita(noAux)
            abertos.put(noAux)           
            return noAux

    return no

def verificaBaixo(no):
    i, j = buscaVazio(no.getTab())
    tab = copy.deepcopy(no.getTab())
    global abertos
    global n
    check = False
    if(-1 < i - 1):
        tab[i][j] = tab[i-1][j]
        tab[i-1][j] = '-'
        aux = copy.deepcopy(tab)
        noAux = Node(no, aux)
        check = verificaRepeticao(noAux)
        if check == False:
            tab[i-1][j] = tab[i][j]
            tab[i][j] = '-'
        if check == True:
            # no.setfilhoBaixo(noAux)  
            abertos.put(noAux) 
            return noAux
    
    return no

def verificaEsquerda(no):
    global abertos
    i, j = buscaVazio(no.getTab())
    tab = copy.deepcopy(no.getTab())
    global n
    check = False
    if(n > j + 1):
        tab[i][j] = tab[i][j+1]
        tab[i][j+1] = '-'
        aux = copy.deepcopy(tab)
        noAux = Node(no, aux)
        check  = verificaRepeticao(noAux)
        if check == False:
            tab[i][j+1] = tab[i][j]
            tab[i][j] = '-'
        if check == True:
            # no.setfilhoEsquerda(noAux)
            abertos.put(noAux)
            return noAux

    return no

def buscaProfundidade(tabuleiroInicial, tabuleiroFinal):
    global abertos
    global fechados
    raiz = Node(None, tabuleiroInicial)
    sucesso = verificaObjetivo(raiz.getTab(), tabuleiroFinal)
    abertos.put(copy.deepcopy(raiz))
    fracasso = False
    check = False
    while(sucesso == False and fracasso == False):
        if abertos.empty():
            fracasso = True
        else:
            no = abertos.get()
            if verificaObjetivo(no.getTab(),tabuleiroFinal):
                sucesso = True
            else:
                aux = verificaCima(no)
                aux = verificaDireita(no)
                aux = verificaBaixo(no)
                aux = verificaEsquerda(no)

                fechados.append(no)
    print(sucesso)
    print(fracasso)