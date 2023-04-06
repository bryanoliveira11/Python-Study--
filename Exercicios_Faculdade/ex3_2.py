lista = [1,5,7]

numeroInicial = lista[0]
posicaoFinal = len(lista) - 1
contaPosicao = posicaoFinal
listaPosicoes = []

while posicaoFinal >= 0:
    listaPosicoes.append(contaPosicao)
    contaPosicao -= 1
    if contaPosicao == 0:
        break
    
listaPosicoes.append(0)

Num_Index = [x*y for x,y in zip(lista,listaPosicoes)]
print(sum(Num_Index))
