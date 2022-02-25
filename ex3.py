print('########## HASHMAT ##########')

entradas = int(input('Digite o número de entradas : '))
entradasCount = 0
hashmatSoldiers = 0
oponentSoldiers = 0
hashmatLista = []
oponentLista = []

def valores() :
    global hashmatSoldiers
    global oponentSoldiers
    hashmatSoldiers = float(input("Digite o número de soldados de hashmat :"))
    oponentSoldiers = float(input("Digite o número de soldados Inimigos :"))
    if(oponentSoldiers > hashmatSoldiers):
        hashmatLista.append(hashmatSoldiers)
        oponentLista.append(oponentSoldiers)


while entradasCount <= entradas:
    print(f'Entrada {entradasCount} :\n')
    if(hashmatSoldiers > oponentSoldiers) :
        print('O número de soldados de Hashmat não deve ser maior do que seu oponente.\n'
              'INFORME OS VALORES NOVAMENTE : \n')
        hashmatLista = []
        oponentLista = []
        entradasCount = 0
    if(entradasCount == entradas):
        print(f'{entradasCount}\n'
        f'{hashmatLista} {oponentLista}\n')
        break
    entradasCount += 1
    valores()

print('VALORES INPUTADOS : \n')

for i in range(len(oponentLista)):  # pega os valores do append na lista oponent, inputada pelo usuário
    print(f'{i}\n')

for i in range(len(hashmatLista)): # pega os valores do append na lista hashmat, inputada pelo usuário
    print(f'{i}\n')
    print (f'HASHMAT : {hashmatLista[i]}  OPONENT {oponentLista[i]}\n')
