from Node import *
import copy
from queue import LifoQueue

import sys

fechados = []
abertos = LifoQueue()
n = 0
m = 0

def verificaObjetivo(tabuleiroAtual, tabuleiroFinal):
    if tabuleiroAtual != tabuleiroFinal: 
        return False
    return True

def buscaVazio(tabuleiroAtual):
    global n
    global m
    for i in range (n):
        for j in range (m):
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
        noAux = Node(no, tab)
        check = verificaRepeticao(noAux)
        if check == True:
            no.setfilhoCima(noAux)
            abertos.put(noAux)
    

def verificaDireita( no):
    i, j = buscaVazio(no.getTab())
    tab = copy.deepcopy(no.getTab())
    global abertos
    check = False
    if(-1 < j - 1):
        tab[i][j] = tab[i][j-1]
        tab[i][j-1] = '-'
        noAux = Node(no, tab)
        check = verificaRepeticao(noAux)
        if check == True:
            no.setfilhoDireita(noAux)
            abertos.put(noAux)           


def verificaBaixo(no):
    i, j = buscaVazio(no.getTab())
    tab = copy.deepcopy(no.getTab())
    global abertos
    check = False
    if(-1 < i - 1):
        tab[i][j] = tab[i-1][j]
        tab[i-1][j] = '-'
        noAux = Node(no, tab)
        check = verificaRepeticao(noAux)
        if check == True:
            no.setfilhoBaixo(noAux)  
            abertos.put(noAux) 
    

def verificaEsquerda(no):
    global abertos
    i, j = buscaVazio(no.getTab())
    tab = copy.deepcopy(no.getTab())
    global m
    check = False
    if(m > j + 1):
        tab[i][j] = tab[i][j+1]
        tab[i][j+1] = '-'
        noAux = Node(no, tab)
        check  = verificaRepeticao(noAux)
        if check == True:
            no.setfilhoEsquerda(noAux)
            abertos.put(noAux)


def buscaProfundidade(tabuleiroInicial, tabuleiroFinal, linha, coluna):
    global abertos
    global fechados
    global n
    global m
    n = linha
    m = coluna
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
                verificaCima(no)
                verificaDireita(no)
                verificaBaixo(no)
                verificaEsquerda(no)
                fechados.append(no)

    if sucesso == True:
        print('Sucesso')
    else: 
        print('Fracasso')