from Node import *
import copy
import time
from queue import Queue

n = 0
m = 0
profundidade = 0
caminho = []
fechados = []
abertos = Queue()

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

def retornaCaminho(no):
    global caminho
    caminho.append(no)
    noAux = no.getPai()
    boolean = False
    while(noAux != None):
        caminho.append(noAux)
        noAux = noAux.getPai()
    caminho.reverse()

def verificaRepeticao(no) :
    global n
    global fechados
    for node in fechados:
        if node.getTab() == no.getTab():
            return False
    return True

def verificaCima(no):
    i, j = buscaVazio(no.getTab())   # Busca a posição do -
    tab = copy.deepcopy(no.getTab())  #cria uma copia do tabuleiro atual
    global abertos 
    global n
    global profundidade
    check = False  #booleano de checagem
    if(n > i + 1):  #Verifica se é possível a peça se mover
        tab[i][j] = tab[i+1][j]         #Faz as mudanças no tabuleiro
        tab[i+1][j] = '-'
        noAux = Node(no, tab)               #Cria nó auxiliar
        noAux.setCusto(no.getCusto() + 1)
        check = verificaRepeticao(noAux)    #verifica se o tabuleiro do nó filho ja esta na lista de fechados
        if check == True:       #Se sim
            no.setfilhoCima(noAux)    #seta ele como filho
            if profundidade < noAux.getCusto():
                profundidade = noAux.getCusto()
            abertos.put(noAux)    #Adiciona ele na lista de abertos
    
def verificaDireita( no):
    i, j = buscaVazio(no.getTab())
    tab = copy.deepcopy(no.getTab())
    global abertos
    global profundidade
    check = False
    if(-1 < j - 1):
        tab[i][j] = tab[i][j-1]
        tab[i][j-1] = '-'
        noAux = Node(no, tab)
        noAux.setCusto(no.getCusto() + 1)
        check = verificaRepeticao(noAux)
        if check == True:
            no.setfilhoDireita(noAux)
            if profundidade < noAux.getCusto():
                profundidade = noAux.getCusto()
            abertos.put(noAux)           

def verificaBaixo(no):
    i, j = buscaVazio(no.getTab()) 
    tab = copy.deepcopy(no.getTab())
    global abertos
    global profundidade
    check = False
    if(-1 < i - 1):
        tab[i][j] = tab[i-1][j]
        tab[i-1][j] = '-'
        noAux = Node(no, tab)
        noAux.setCusto(no.getCusto() + 1)
        check = verificaRepeticao(noAux)
        if check == True:
            no.setfilhoBaixo(noAux)  
            if profundidade < noAux.getCusto():
                profundidade = noAux.getCusto()
            abertos.put(noAux) 
    
def verificaEsquerda(no):
    global abertos
    i, j = buscaVazio(no.getTab())
    tab = copy.deepcopy(no.getTab())
    global n
    global m
    global profundidade
    check = False
    if(m > j + 1):
        tab[i][j] = tab[i][j+1]
        tab[i][j+1] = '-'
        noAux = Node(no, tab)
        noAux.setCusto(no.getCusto() + 1)
        check  = verificaRepeticao(noAux)
        if check == True:
            no.setfilhoEsquerda(noAux)
            if profundidade < noAux.getCusto():
                profundidade = noAux.getCusto()
            abertos.put(noAux)


def buscaLargura(tabuleiroInicial, tabuleiroFinal, linha, coluna):
    print('')
    print('Busca Largura:')
    nos_expandidos = 0
    nos_visitados = 0
    time_init = time.time()
    global abertos
    global fechados
    global n
    global m
    global profundidade
    n = linha
    m = coluna 
    raiz = Node(None,tabuleiroInicial)
    raiz.setCusto(0)
    abertos.put(raiz)
    sucesso = False
    fracasso = False
    check = False
    noResult = None
    while(sucesso == False and fracasso == False):
        if abertos.empty():
            fracasso = True
        else:
            no = abertos.get()
            if verificaObjetivo(no.getTab(),tabuleiroFinal):
                noResult = no
                sucesso = True
            else:
                verificaCima(no)
                verificaDireita(no)
                verificaBaixo(no)
                verificaEsquerda(no)
                fechados.append(no)
            # print(no.getTab())
    time_end = time.time()
    print('Tempo de execução: ' + str(time_end - time_init))
    nos_visitados = len(fechados)
    nos_expandidos = abertos.qsize() + nos_visitados
    print('Nos visitados: ' + str(nos_visitados))
    print('Nos expandidos: ' + str(nos_expandidos))
    print('Profundidade:' + str(profundidade))
    print('Fator médio de ramificação:' + str((nos_expandidos-1)/ nos_visitados))
    if sucesso == True:
        retornaCaminho(noResult)
        print('Custo Solução:' + str(noResult.getCusto()))
        # print('Caminho:')
        # for aux in caminho:
        #     print(aux.getTab())
