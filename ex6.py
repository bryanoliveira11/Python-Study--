frutas = ['laranja', 'maca', 'pera', 'banana', 'kiwi', 'maca', 'banana']

InputNome = str(input('Fruta que deseja Mostrar a Última Posição : ')).lower()
count = 0

while count <= 6:
    if InputNome != frutas[count]:
        print('Não tem essa Fruta na Lista !')
    count += 1
else:
    print(f'A Última Ocorrência de {InputNome} é {len(frutas) - frutas[-1::-1].index(InputNome) -1}')
