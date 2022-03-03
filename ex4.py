testCounter = nCounter = 1
numLista = []

testes = int(input('Número de testes : '))
    
while nCounter <= testes:
    num_valor = int(input('Valores : (−1000 ≤ n ≤ 1000) : '))
    print(f'Teste {testCounter}\n')
    if num_valor > 1000 or num_valor < -1000:
        print('O número não pode ser acima de 1000 e nem abaixo de -1000 !!\n')
    else:
        testCounter += 1
        nCounter += 1
        numLista.append(num_valor)

for i in range(len(numLista)):
    resultado = []
    dezenas = []
    resultado.append(numLista[i] * 567 / 9 + 7492 * 235 / 47 - 498)
    for i in range(len(resultado)) :
        dezenas.append(((resultado[i] // 10) % 10))
        print(f'{resultado}' , f'dezenas = {dezenas}')
        

# “Multiplique n por 567, depois divida o resultado por 9, some 7492, multiplique por 235, divida por 47 e subtraia 498.
# (numLista[i] * (567 / 9 + 7492 * 235 / 47 - 498))
