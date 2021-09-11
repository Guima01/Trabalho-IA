from Node import *
import copy
import time
from queue import Queue

n = 0
m = 0
profundidade = 0
profundidadeAux = 0
caminho = []
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

def verificaRepeticao(no) :
    noAux = no.getPai()
    boolean = False
    while(noAux != None):
        if noAux.getTab() == no.getTab():
            return False
        noAux = noAux.getPai()
    return True

def retornaCaminho(no):
    global caminho
    caminho.append(no)
    noAux = no.getPai()
    boolean = False
    while(noAux != None):
        caminho.append(noAux)
        noAux = noAux.getPai()
    caminho.reverse()

def verificaCima(no):
    i, j = buscaVazio(no.getTab())
    tab = copy.deepcopy(no.getTab())
    global n
    global m
    check = False
    if(n > i + 1 and no.getfilhoCima() == None):
        tab[i][j] = tab[i+1][j]
        tab[i+1][j] = '-'
        noAux = Node(no, tab)
        noAux.setCusto(no.getCusto() + 1)
        check = verificaRepeticao(noAux)
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
        noAux = Node(no, tab)
        noAux.setCusto(no.getCusto() + 1)
        check = verificaRepeticao(noAux)
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
        noAux = Node(no, tab)
        noAux.setCusto(no.getCusto() + 1)
        check = verificaRepeticao(noAux)
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
        noAux = Node(no, tab)
        noAux.setCusto(no.getCusto() + 1)
        check  = verificaRepeticao(noAux)
        if check == True:
            no.setfilhoEsquerda(noAux)
            return noAux, check 

    return no, check

def backTracking (tabuleiroInicial, tabuleiroFinal, linha, coluna):
    print('')
    print('BackTracking:')
    nos_expandidos = 0
    nos_visitados = 0
    time_init = time.time()
    global n
    global m 
    global profundidade
    global profundidadeAux
    folha = 0
    n = linha
    m = coluna   
    raiz = Node(None, copy.deepcopy(tabuleiroInicial))
    raiz.setCusto(0)
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
            nos_visitados = nos_visitados + 1
            profundidadeAux = profundidadeAux + 1
            if profundidade < profundidadeAux:
                profundidade = profundidadeAux
            sucesso = verificaObjetivo(no.getTab(),tabuleiroFinal)

        elif check == False:
            profundidadeAux = profundidadeAux - 1
            if no.getfilhoBaixo() == None and no.getfilhoCima() == None and no.getfilhoDireita() == None and no.getfilhoEsquerda() == None:
                folha += 1
            no = no.getPai()
            if no == None:
                fracasso = True
        # print(no.getTab())
    folha += 1
    time_end = time.time()
    nos_expandidos = nos_visitados
    print('Tempo de execução: ' + str(time_end - time_init))
    print('Nos visitados: ' + str(nos_visitados))
    print('Nos expandidos: ' + str(nos_expandidos))
    print('Profundidade:' + str(profundidade))
    print('Fator médio de ramificação:' + str((nos_expandidos-1)/ (nos_visitados - folha)))
    if sucesso == True:
        retornaCaminho(no)
        print('Custo Solução:' + str(no.getCusto()))
        # print('Caminho:')
        # for aux in caminho:
        #     print(aux.getTab())