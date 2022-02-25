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
    if(hashmatSoldiers > oponentSoldiers) :
        print('O número de soldados de Hashmat não deve ser maior do que seu oponente.\n')
        hashmatLista = []
        oponentLista = []
        entradasCount = 0
    if(entradasCount == entradas):
        print(f'{entradasCount}\n'
        f'{hashmatLista} {oponentLista}')
        break
    entradasCount += 1
    valores()
    
