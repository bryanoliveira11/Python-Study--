print('########## HASHMAT ##########')

entradas = int(input('Digite o número de entradas : '))
entradasCount = hashmatSoldiers = oponentSoldiers = 0
hashmatLista = []
oponentLista = []

def valores() :
    global hashmatSoldiers
    global oponentSoldiers
    oponentSoldiers = int(input("Digite o número de soldados Inimigos :"))
    hashmatSoldiers = int(input("Digite o número de soldados de hashmat :"))
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
        break
    entradasCount += 1
    valores()

print('VALORES INPUTADOS : \n')

for i in range(len(oponentLista) and len(hashmatLista)):  # pega os valores do append nas listas, inputada pelo usuário
     print (f'OPONENT {oponentLista[i]}  HASHMAT : {hashmatLista[i]}\n')
     
print('#### RESULTADOS ####')
for i in range(len(oponentLista)):
    resultado = []
    resultado.append(oponentLista[i] - hashmatLista[i])
    print(f'''   
        {resultado}''')
