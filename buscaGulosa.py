from Node import *
import copy
from queue import Queue

n = 0
m = 0
fechados = []
abertos = []
tabFinal = []

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
    global tabFinal
    check = False  #booleano de checagem
    if(n > i + 1):  #Verifica se é possível a peça se mover
        tab[i][j] = tab[i+1][j]         #Faz as mudanças no tabuleiro
        tab[i+1][j] = '-'
        noAux = Node(no, tab)               #Cria nó auxiliar
        noAux.setCustoGuloso(calcManhatann(noAux.getTab(),tabFinal))
        check = verificaRepeticao(noAux)    #verifica se o tabuleiro do nó filho ja esta na lista de fechados
        if check == True:       #Se sim
            no.setfilhoCima(noAux)    #seta ele como filho
            abertos.append(noAux)    #Adiciona ele na lista de abertos
    
def verificaDireita( no):
    i, j = buscaVazio(no.getTab())
    tab = copy.deepcopy(no.getTab())
    global abertos
    global tabFinal
    check = False
    if(-1 < j - 1):
        tab[i][j] = tab[i][j-1]
        tab[i][j-1] = '-'
        noAux = Node(no, tab)
        noAux.setCustoGuloso(calcManhatann(noAux.getTab(),tabFinal))
        check = verificaRepeticao(noAux)
        if check == True:
            no.setfilhoDireita(noAux)
            abertos.append(noAux)           

def verificaBaixo(no):
    i, j = buscaVazio(no.getTab()) 
    tab = copy.deepcopy(no.getTab())
    global abertos
    global tabFinal
    check = False
    if(-1 < i - 1):
        tab[i][j] = tab[i-1][j]
        tab[i-1][j] = '-'
        noAux = Node(no, tab)
        noAux.setCustoGuloso(calcManhatann(noAux.getTab(),tabFinal))
        check = verificaRepeticao(noAux)
        if check == True:
            no.setfilhoBaixo(noAux)  
            abertos.append(noAux) 
    
def verificaEsquerda(no):
    i, j = buscaVazio(no.getTab())
    tab = copy.deepcopy(no.getTab())
    global abertos
    global n
    global m
    global tabFinal
    check = False
    if(m > j + 1):
        tab[i][j] = tab[i][j+1]
        tab[i][j+1] = '-'
        noAux = Node(no, tab)
        noAux.setCustoGuloso(calcManhatann(noAux.getTab(),tabFinal))
        check  = verificaRepeticao(noAux)
        if check == True:
            no.setfilhoEsquerda(noAux)
            abertos.append(noAux)

def buscaGulosa(tabuleiroInicial, tabuleiroFinal, linha, coluna):
    global abertos
    global fechados
    global n
    global m
    global tabFinal
    tabFinal = tabuleiroFinal
    n = linha
    m = coluna 
    raiz = Node(None,tabuleiroInicial)
    raiz.setCustoGuloso(calcManhatann(raiz.getTab(),tabuleiroFinal))
    abertos.append(raiz)
    sucesso = False
    fracasso = False
    check = False
    while(sucesso == False and fracasso == False):
        if len(abertos) == 0:
            fracasso = True
        else:
            i = 0                                                            #Diferença basicamente são nas linhas (115 até 124)
            menor = -1                                                      
            for i in range(len(abertos)):
                if abertos[i].getCustoGuloso() < menor or menor == -1:
                    menor = abertos[i].getCustoGuloso()
            i = 0
            for i in range(len(abertos)):
                if abertos[i].getCustoGuloso() == menor:
                    no = abertos.pop(i)
                    break
            fechados.append(no)
            if verificaObjetivo(no.getTab(),tabuleiroFinal):
                sucesso = True
            else:
                verificaCima(no)
                verificaDireita(no)
                verificaBaixo(no)
                verificaEsquerda(no)

    if sucesso == True:
        print('Sucesso')
    else: 
        print('Fracasso')