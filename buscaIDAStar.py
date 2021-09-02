from Node import *
import copy
import time
from queue import Queue

n = 0
m = 0
profundidade = 0
patamar = None
patamar_old = -1
caminho = []
tabFinal = []
descartados = None

def verificaObjetivo(tabuleiroAtual, tabuleiroFinal):
    if tabuleiroAtual != tabuleiroFinal: 
        return False
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

def buscaVazio(tabuleiroAtual):
    global n
    global m
    for i in range (n):
        for j in range (m):
            if tabuleiroAtual[i][j] == '-':
                return i,j

#Função pra calcular a heurística utilizada
def calcManhatann(tabuleiroAtual, tabuleiroFinal):
    global n
    global m
    value = 0
    number = 0
    check = False
    for i in range (n):
        for j in range (m):
            number = tabuleiroFinal[i][j]
            if number != '-':
                for k in range (n):
                    for l in range (m):
                        if number == tabuleiroAtual[k][l]:
                            value += (abs(k - i) + abs(j - l))
                            check = True
                            break
                    if check == True:
                        check = False
                        break
    return value

def verificaRepeticao(no) :
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
    # print('Cima')
    # print(no.getfilhoCima())
    if(n > i + 1 and no.getfilhoCima() == None):
        tab[i][j] = tab[i+1][j]
        tab[i+1][j] = '-'
        noAux = Node(no, tab)
        noAux.setCustoGuloso(calcManhatann(noAux.getTab(),tabFinal))
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
    # print('Direita')
    # print(no.getfilhoDireita())
    if(-1 < j - 1 and no.getfilhoDireita() == None):
        tab[i][j] = tab[i][j-1]
        tab[i][j-1] = '-'
        noAux = Node(no, tab)
        noAux.setCustoGuloso(calcManhatann(noAux.getTab(),tabFinal))
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
    # print('Baixo')
    # print(no.getfilhoBaixo())
    if(-1 < i - 1 and no.getfilhoBaixo() == None):
        tab[i][j] = tab[i-1][j]
        tab[i-1][j] = '-'
        noAux = Node(no, tab)
        noAux.setCustoGuloso(calcManhatann(noAux.getTab(),tabFinal))
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
    # print('Esquerda')
    # print(no.getfilhoEsquerda())
    if(m > j + 1 and no.getfilhoEsquerda() == None):
        tab[i][j] = tab[i][j+1]
        tab[i][j+1] = '-'
        noAux = Node(no, tab)
        noAux.setCustoGuloso(calcManhatann(noAux.getTab(),tabFinal))
        noAux.setCusto(no.getCusto() + 1)
        check = verificaRepeticao(noAux)
        if check == True:
            no.setfilhoEsquerda(noAux)
            return noAux, check 
    return no, check

def buscaIDAStar(tabuleiroInicial, tabuleiroFinal, linha, coluna):
    print('')
    print('Busca IDA*:')
    nos_expandidos = 0
    nos_visitados = 0
    time_init = time.time()
    global n
    global m
    global tabFinal
    global patamar
    global patamar_old
    global descartados
    tabFinal = tabuleiroFinal
    n = linha
    m = coluna 
    raiz = Node(None,tabuleiroInicial)
    raiz.setCustoGuloso(calcManhatann(raiz.getTab(),tabuleiroFinal))
    raiz.setCusto(0)
    patamar = raiz.getCustoGuloso() + raiz.getCusto()
    no = raiz
    sucesso = False
    fracasso = False
    check = False
    noResult = None
    while(sucesso == False and fracasso == False):
        if patamar_old == patamar:
            fracasso = True
        else:
            if verificaObjetivo(no.getTab(),tabuleiroFinal) and no.getCustoGuloso() + no.getCusto() <= patamar:
                sucesso = True
            else:
                if no.getCusto() + no.getCustoGuloso() > patamar:
                        if descartados == None:
                            descartados = no.getCusto() + no.getCustoGuloso()
                        elif descartados > no.getCusto() + no.getCustoGuloso():
                            descartados = no.getCusto() + no.getCustoGuloso()
                        no = no.getPai()

                no, check = verificaCima(no)
                if check == False:
                    # print('A')
                    # print(no)
                    # print(check)
                    no, check = verificaDireita(no)
                    # print('B')
                    # print(no)
                    # print(check)
                if check == False:
                    no, check = verificaBaixo(no)
                    # print('C')
                    # print(no)
                    # print(check)
                if check == False:
                    no, check = verificaEsquerda(no)
                    # print('D')
                    # print(no)
                    # print(check)
                if check == False:
                    if no == raiz:
                        patamar_old = patamar
                        patamar = descartados
                    else:
                        no = no.getPai()

    time_end = time.time()
    print('Tempo de execução: ' + str(time_end - time_init))
    if sucesso == True:
        print('Brabo')
    #     retornaCaminho(noResult)
    #     nos_visitados = len(fechados)
    #     nos_expandidos = len(abertos) + nos_visitados
    #     print('Custo Solução:' + str(noResult.getCusto()) )
    #     print('Nos visitados: ' + str(nos_visitados))
    #     print('Nos expandidos: ' + str(nos_expandidos))
    #     print('Profundidade:' + str(profundidade))
    #     print('Fator médio de ramificação:' + str((nos_expandidos-1)/ nos_visitados))
    #     print('Caminho:')
    #     for aux in caminho:
    #         print(aux.getTab())
    else: 
        print('Fracasso')