import copy
from Node import *
from buscaLargura import *
from buscaProfundidade import *
from backTracking import *
from buscaOrdenada import *
from buscaGulosa import *
from buscaAStar import *
from buscaIDAStar import *

n = 0 # linha
m = 0 #coluna


# ordem Backtracking:
# Baixo
# Esquerda
# Cima
# Direita



def main():
    global n
    global m
    tabuleiroInicial = []
    tabuleiroFinal = []

    print('Digite a proporção da matriz')
    n = int(input())
    m = int(input()) 
    print("Digite o estado Inicial da tabela")
    for i in range (n):
        tabuleiroInicial.append([])
        for j in range (m):
            tabuleiroInicial[i].append(input())

    print("Digite o estado final da tabela")
    for i in range (n):
        tabuleiroFinal.append([])
        for j in range (m):
            tabuleiroFinal[i].append(input())

    backTracking(tabuleiroInicial, tabuleiroFinal, n, m)
    buscaLargura(tabuleiroInicial, tabuleiroFinal, n, m)
    buscaProfundidade(tabuleiroInicial, tabuleiroFinal, n, m)
    buscaOrdenada(tabuleiroInicial, tabuleiroFinal, n, m)
    buscaGulosa(tabuleiroInicial, tabuleiroFinal, n, m)
    buscaAStar(tabuleiroInicial, tabuleiroFinal, n, m)
    buscaIDAStar(tabuleiroInicial, tabuleiroFinal, n, m)

main()