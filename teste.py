from time import sleep

firstMatrix = [
    ['.', '.', '.', '.', '11', '.', '22', '.'],
    ['.', '.', '.', '.', '.', '.', '11', '.'],
    ['.', '.', '.', '.', '.', '.', '11', '.'],
    ['.', '.', '.', '.', '.', '.', '11', '.'],
    ['.', '.', '.', '.', '.', '.', '11', '3'],
    ['.', '.', '.', '.', '.', '.', '11', '.'],
    ['.', '.', '.', '.', '.', '.', '11', '.'],
    ['.', '.', '.', '.', '.', '.', '11', '.'],
]
forcaInicial = int(input())
posicaoInicial = tuple(map(int,input().split(" ")))

def converterVizinhos(posicaoAtual : tuple, matrizBase:list):
    for i in [-1,0,1]:
        for j in [-1,0,1]:

            if posicaoAtual[0] + i >= 0 and posicaoAtual[1] + j >= 0 and posicaoAtual[0] + i <= len(matrizBase)-1 and posicaoAtual[1] + j <= len(matrizBase)-1 and j != i:
                if matrizBase[posicaoAtual[0] + i][posicaoAtual[1] + j] == "A":
                    pass
                elif matrizBase[posicaoAtual[0] + i][posicaoAtual[1] + j] == '.' or int(matrizBase[posicaoAtual[0] + i][posicaoAtual[1] + j]) <= forcaInicial :
                    matrizBase[posicaoAtual[0] + i][posicaoAtual[1] + j] = 'A'

def haVizinhosNaoVerificados(posicaoAtual : tuple, matrizbase: list):
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if posicaoAtual[0] + i >= 0 and posicaoAtual[1] + j >= 0 and posicaoAtual[0] + i <= len(matrizbase)-1 and posicaoAtual[1] + j <= len(matrizbase)-1 and i != j:
                if matrizbase[posicaoAtual[0] + i][posicaoAtual[1] + j] == "A":
                    pass
                elif matrizbase[posicaoAtual[0] + i][posicaoAtual[1] + j] == '.' or int(matrizbase[posicaoAtual[0] + i][posicaoAtual[1] + j]) <= forcaInicial :
                    return True

    return False
firstMatrix[posicaoInicial[0]][posicaoInicial[1]] = 'A'
posicaoAlterada = True
while True:
    continuar = False
    for lista in firstMatrix:
        if '.' in lista:
            continuar = True
    if not posicaoAlterada:
        print("DEADLOCK")
        break
    if continuar:
        posicaoAlterada = False
        for item in range(len(firstMatrix)):
            for posicao in range(len(firstMatrix[0])):
                if firstMatrix[item][posicao] == 'A' and haVizinhosNaoVerificados((item,posicao),firstMatrix):
                    if not posicaoAlterada:
                        posicaoAtual = (item,posicao)
                        posicaoAlterada = True

        converterVizinhos(posicaoAtual,firstMatrix)


        for linhaMatriz in firstMatrix:
            print(linhaMatriz)
        # sleep(2)
    else:
        break























