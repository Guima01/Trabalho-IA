#include <iostream>
#include <string>
using namespace std;

struct Node
{
    // stores the parent node of the current node
    // helps in tracing path when the answer is found
    Node* parent;
 
    // stores matrix
    int mat[3][3];
 
    int id;
 
//     // stores the number of misplaced tiles
//     int cost;
 
//     // stores the number of moves so far
//     int level;
};

//ordem:
//Cima 
//Direita
//Baixo
//Esquerda
void backtracking (int &tabuleiroInicial, int &tabuleiroFinal){
    bool sucesso = false;

    while (!sucesso){
    }
}

int main()
{
    char tabuleiroInicial[3][3];
    char tabuleiroFinal[3][3];
    cout << "Digite o estado inicial da tabela"<<endl;
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cin >> tabuleiroInicial[i][j];
        }
    }
    cout << "Digite o estado final da tabela";
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cin >> tabuleiroFinal[i][j];
        }
    }
    for (int l = 0; l < 3; l++)
    {
        for (int c = 0; c < 3; c++)
        {
            cout << tabuleiroInicial[l][c] << " ";
        }
        cout << "\n";
    }
        for (int l = 0; l < 3; l++)
    {
        for (int c = 0; c < 3; c++)
        {
            cout << tabuleiroFinal[l][c] << " ";
        }
        cout << "\n";
    }
    return 0;
}