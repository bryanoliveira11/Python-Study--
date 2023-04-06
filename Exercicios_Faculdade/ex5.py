testCounter = nCounter = 1
velocidadeLista = []
tempoLista = []
tempoDobrado = []

def calculos():
    print('##### RESULTADOS #####\n')
    for i in range(len(tempoDobrado)):
        calculo = velocidadeLista[i] * tempoDobrado[i]
        print(f'VELOCIDADES {calculo}')

testes = int(input('Número de testes : '))
    
while nCounter <= testes:
    velocidade = int(input('Digite a Velocidade (−100 ≤ v ≤ 100) :'))
    tempo = int(input('Digite o tempo (0 ≤ t ≤ 200) :'))
    print(f'Teste {testCounter}\n')
    if velocidade > 100 or velocidade < -100 or tempo > 200 or tempo < 0:
        print(f'                    Há algo de errado ! \n'
              'Lembre-se : Velocidade (−100 ≤ v ≤ 100) e tempo (0 ≤ t ≤ 200).\n')
        nCounter = 1
        velocidadeLista = []
        tempoLista = []
    else:
        testCounter += 1
        nCounter += 1
        print(f'Valor de Velocidade {velocidade} adicionado !')
        print(f'Valor de Tempo {tempo} adicionado !\n')
        velocidadeLista.append(velocidade)
        tempoLista.append(tempo)
        tempoDobrado.append(tempo * 2)
    
print(f'Velocidades = {velocidadeLista}')
print(f'Tempos = {tempoLista}\n')
calculos()

    
    
    
    
    
# Para cada linha de entrada imprima um único inteiro em uma linha denotando o deslocamento em dobro daquele tempo.
# multiplicar o dobro do tempo pela vel
