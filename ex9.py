#Pedir ao usuário um número “x”, e somar os elementos da lista desde o começo até a posição “x”, incluindo-lhe. 

lista = [1, 5, 7, 9, 3]

posicao = int(input('Posição Final da soma : '))
count = soma = 0
somaLista = []

if posicao > 4 or posicao < 0:
    print('Posição Inválida !')
else:
    while count <= posicao:
        somaLista.append(lista[0:posicao+1])
        break
    count += 1
    for numeros in somaLista[0]:
        soma += numeros
    print(soma)
        
    