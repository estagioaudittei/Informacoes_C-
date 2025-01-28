# matriz com ponderamento

matriz = [
    ['0', '99999999999999',  '0',   '0',   '1',   '0','0','0'],
    ['0',  '10'          ,   '0',   '0',   '500', '0','0','0'],
    ['1', '100',             '0',   '0',   '500', '0','0','0'],
    ['0',  '0',              '0',   '0',   '500', '0','0','0'],
    ['300','300',            '100','500',  '0',   '0','0','0'],
    ['0',  '0',              '0',   '0',   '0',   '0','0','0'],
    ['0',  '0',              '0',   '0',   '0',   '0','0','0'],
    ['0',  '0',              '0',   '0',   '0',   '0','0','0'],
]

obj = (7,7)
inicio = (0,0)
caminho = dict()
caminho[inicio] = None
proximosNaFila = [(inicio[0],inicio[1],0)]
jaAnalisados = [inicio]

def alterarMatriz(posicao):

    matriz[posicao[0]][posicao[1]] = 'A'

def adicionarVizinhos(posicao_custo):
    if not any(posicao_custo == (prioridade[0],prioridade[1]) for prioridade in proximosNaFila):
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                if posicao_custo[0] + x >= 0 and posicao_custo[0] + x < len(matriz[0]) and posicao_custo[1] + y >= 0 and posicao_custo[1] + y < len(matriz) and abs(x) != abs(y):
                    if (posicao_custo[0] + x, posicao_custo[1] + y ) not in jaAnalisados and (posicao_custo[0] + x, posicao_custo[1] + y, int(  matriz[posicao_custo[0]+x]  [posicao_custo[1]+ y] ) ) not in proximosNaFila:
                        proximosNaFila.append((posicao_custo[0] + x,posicao_custo[1] + y,( int(  matriz[posicao_custo[0]+x]  [posicao_custo[1]+ y] ) + int(matriz[posicao_custo[0]][posicao_custo[1]]) )  ) )

contador = 0
while proximosNaFila != []:
    print(proximosNaFila)
    posicoes_custo = (proximosNaFila[0][0],proximosNaFila[0][1],int(matriz[proximosNaFila[0][0]][proximosNaFila[0][1]]))
    jaAnalisados.append((posicoes_custo[0], posicoes_custo[1]))
    adicionarVizinhos(posicoes_custo)
    alterarMatriz(posicoes_custo)
    proximosNaFila.pop(0)
    proximosNaFila.sort(key= lambda x : x[2])
    for linha in matriz:
        print(linha)
    if (posicoes_custo[0],posicoes_custo[1]) == obj:
        print("FIM")
        break

