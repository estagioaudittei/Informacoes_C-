from time import sleep

caminhos = dict()

ja_visitados = []
forca = int(input())
posicaoInicial = tuple(map(int,input().split(' ')))
proximos_na_fila = []
proximos_na_fila.append(posicaoInicial)
caminhos[posicaoInicial] = None
matriz = [
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','#','.'],
    ['.','.','.','.','.','.','#','.'],
    ['.','.','.','.','.','.','#','.'],
    ['.','.','.','.','.','.','#','.'],
    ['.','.','.','.','.','.','#','K'],
]
Objetivo = tuple()
for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        if matriz[linha][coluna] == 'K':
            Objetivo = (linha,coluna)
            break



def adicionarVizinhosNaFila(posicaoAtual : tuple):
    for proximos_x in [-1,0,1]:
        for proximos_y in [-1,0,1]:
            if posicaoAtual[0] + proximos_x >= 0 and posicaoAtual[0] + proximos_x < len(matriz[0]) and posicaoAtual[1] + proximos_y >= 0 and posicaoAtual[1]  + proximos_y < len(matriz):
                if (posicaoAtual[0] + proximos_x, posicaoAtual[1] + proximos_y) not in ja_visitados and (posicaoAtual[0] + proximos_x, posicaoAtual[1] + proximos_y) not in proximos_na_fila and matriz[posicaoAtual[0] + proximos_x][posicaoAtual[1] + proximos_y] != "#":
                    proximos_na_fila.append((posicaoAtual[0] + proximos_x, posicaoAtual[1] + proximos_y))
                    caminhos[(posicaoAtual[0] + proximos_x, posicaoAtual[1] + proximos_y)] = posicaoAtual




for item in proximos_na_fila:

    matriz[item[0]][item[1]] = 'A'

    for linha in matriz:
        print(linha)
    adicionarVizinhosNaFila(item)
    if item == Objetivo:
        resposta = []
        while True:
            if caminhos[item] == None:
                break
            else:
                resposta.append(item)
                item =  caminhos[item]
        print("O minimo de passos para chegar até o objetivo é: ", len(resposta))

        # print("Chegou =D")
        # print(caminhos)
        break



















