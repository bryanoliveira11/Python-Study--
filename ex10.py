#Pedir ao usuário dois números “x” e “y”, e mostrar a soma dos elementos da lista a partir da posição “x” até a posição “y”, incluindo. 

lista = [1, 5, 7, 9, 3]

posicaoInicial = int(input('Posição Inicial da soma : '))
posicaoFinal = int(input('Posição Final da soma : '))
count = soma = 0
somaLista = []

if posicaoInicial > 4 or posicaoInicial < 0 or posicaoFinal > 4 or posicaoFinal < 0 or posicaoInicial > posicaoFinal:
    print('Posicões Inválidas !')
else:
    while count <= posicaoFinal:
        somaLista.append(lista[posicaoInicial:posicaoFinal+1])
        break
    count += 1
    for numeros in somaLista[0]:
        soma += numeros
    print(soma)
        
    