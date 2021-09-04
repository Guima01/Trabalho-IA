from Node import *
import copy
import time
from queue import Queue

n = 0
m = 0
profundidade = 0
profundidadeAux = 0
nos_visitados = 0
nos_expandidos = 0
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
    global nos_visitados
    global profundidade
    global profundidadeAux
    check = False
    if(n > i + 1 and no.getfilhoCima() == None):
        tab[i][j] = tab[i+1][j]
        tab[i+1][j] = '-'
        noAux = Node(no, tab)
        noAux.setCustoGuloso(calcManhatann(noAux.getTab(),tabFinal))
        noAux.setCusto(no.getCusto() + 1)
        check = verificaRepeticao(noAux)
        if check == True:
            nos_visitados += 1
            profundidadeAux = profundidadeAux + 1
            if profundidade < profundidadeAux:
                profundidade = profundidadeAux
            no.setfilhoCima(noAux)
            return noAux, check
    return no, check

def verificaDireita( no):
    i, j = buscaVazio(no.getTab())
    tab = copy.deepcopy(no.getTab())
    global nos_visitados
    global profundidade
    global profundidadeAux
    check = False
    if(-1 < j - 1 and no.getfilhoDireita() == None):
        tab[i][j] = tab[i][j-1]
        tab[i][j-1] = '-'
        noAux = Node(no, tab)
        noAux.setCustoGuloso(calcManhatann(noAux.getTab(),tabFinal))
        noAux.setCusto(no.getCusto() + 1)
        check = verificaRepeticao(noAux)
        if check == True:
            no.setfilhoDireita(noAux)
            profundidadeAux = profundidadeAux + 1
            if profundidade < profundidadeAux:
                profundidade = profundidadeAux
            nos_visitados += 1
            return noAux, check

    return no, check

def verificaBaixo(no):
    i, j = buscaVazio(no.getTab())
    tab = copy.deepcopy(no.getTab())
    global nos_visitados
    global profundidade
    global profundidadeAux
    check = False
    if(-1 < i - 1 and no.getfilhoBaixo() == None):
        tab[i][j] = tab[i-1][j]
        tab[i-1][j] = '-'
        noAux = Node(no, tab)
        noAux.setCustoGuloso(calcManhatann(noAux.getTab(),tabFinal))
        noAux.setCusto(no.getCusto() + 1)
        check = verificaRepeticao(noAux)
        if check == True:
            no.setfilhoBaixo(noAux)
            profundidadeAux = profundidadeAux + 1
            if profundidade < profundidadeAux:
                profundidade = profundidadeAux
            nos_visitados += 1  
            return noAux, check
    
    return no, check

def verificaEsquerda(no):
    i, j = buscaVazio(no.getTab())
    tab = copy.deepcopy(no.getTab())
    global n
    global m
    global nos_visitados
    global profundidade
    global profundidadeAux
    check = False
    if(m > j + 1 and no.getfilhoEsquerda() == None):
        tab[i][j] = tab[i][j+1]
        tab[i][j+1] = '-'
        noAux = Node(no, tab)
        noAux.setCustoGuloso(calcManhatann(noAux.getTab(),tabFinal))
        noAux.setCusto(no.getCusto() + 1)
        check = verificaRepeticao(noAux)
        if check == True:
            no.setfilhoEsquerda(noAux)
            profundidadeAux = profundidadeAux + 1
            if profundidade < profundidadeAux:
                profundidade = profundidadeAux
            nos_visitados += 1
            return noAux, check 
    return no, check

def buscaIDAStar(tabuleiroInicial, tabuleiroFinal, linha, coluna):
    print('')
    print('Busca IDA*:')
    time_init = time.time()
    global nos_visitados
    global nos_expandidos
    global n
    global m
    global tabFinal
    global patamar
    global patamar_old
    global descartados
    global profundidade
    global profundidadeAux
    tabFinal = tabuleiroFinal
    folha = 0
    n = linha
    m = coluna 
    raiz = Node(None,tabuleiroInicial)
    raiz.setCustoGuloso(calcManhatann(raiz.getTab(),tabuleiroFinal))
    raiz.setCusto(0)
    patamar = raiz.getCustoGuloso() + raiz.getCusto()
    s = copy.deepcopy(raiz)
    no = s
    nos_expandidos += 1
    sucesso = False
    fracasso = False
    check = False
    noResult = None
    while(sucesso == False and fracasso == False):
        if patamar_old == patamar or patamar == None:
            fracasso = True
        else:
            if verificaObjetivo(no.getTab(),tabuleiroFinal) and no.getCustoGuloso() + no.getCusto() <= patamar:
                noResult = no
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
                    no, check = verificaDireita(no)
                if check == False:
                    no, check = verificaBaixo(no)
                if check == False:
                    no, check = verificaEsquerda(no)
                if check == False:
                    if no == s:
                        patamar_old = patamar
                        patamar = descartados
                        s = copy.deepcopy(raiz)
                        no = s
                        descartados = None
                        profundidade = 0
                        profundidadeAux = 0
                        folha = 0
                        nos_expandidos = 0
                        nos_visitados = 0
                        
                    else:
                        profundidadeAux -= 1
                        folha += 1
                        no = no.getPai() 

    print
    time_end = time.time()
    folha += 1
    nos_expandidos =  nos_visitados
    print('Tempo de execução: ' + str(time_end - time_init))
    print('Nos visitados: ' + str(nos_visitados))
    print('Nos expandidos: ' + str(nos_expandidos))
    print('Profundidade:' + str(profundidade))
    print('Fator médio de ramificação:' + str((nos_expandidos-1)/ (nos_visitados - folha)))
    if sucesso == True:
        retornaCaminho(noResult)
        print('Custo Solução:' + str(noResult.getCusto()))
        # print('Caminho:')
        # for aux in caminho:
        #     print(aux.getTab())