import copy
from Node import *
from buscaLargura import *
from buscaProfundidade import *
from backTracking import *
n = 3


# ordem Backtracking:
# Cima 
# Direita
# Baixo
# Esquerda



def main():
    global n
    tabuleiroInicial = []
    tabuleiroFinal = []
    print("Digite o estado Inicial da tabela")
    for i in range (n):
        tabuleiroInicial.append([])
        for j in range (n):
            tabuleiroInicial[i].append(input())

    print("Digite o estado final da tabela")
    for i in range (n):
        tabuleiroFinal.append([])
        for j in range (n):
            tabuleiroFinal[i].append(input())

    # backTracking(tabuleiroInicial, tabuleiroFinal)
    # buscaLargura(tabuleiroInicial, tabuleiroFinal)
    # buscaProfundidade(tabuleiroInicial, tabuleiroFinal)

main()