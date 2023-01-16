import time

from methods import Bot

while True:
    marcacoes = input('Digite a lista de @ que deseja marcar: ').split()
    quantidade = int(input('Quantidade de @ que deseja marcar (máx 5): '))

    if quantidade > 4 or quantidade < 1:
        print('Por favor, digite um número entre 1 e 5\n')
    elif len(marcacoes) < quantidade or len(marcacoes) == 0:
        print('Por favor, digite uma lista de @ >= 1 e < que a quantidade de @ que deseja marcar\n')
    else:
        break


obj = Bot(marcacoes, quantidade)

while True:
    tempo = int(input('Tempo de espera entre as marcações (recomendado 60): '))
    if tempo > 0:
        break

quantidade = 1
time.sleep(5)

while True:
    obj.comentar()
    time.sleep(tempo)
    quantidade += 1
    print(f'Quantidade de marcações já feitas: {quantidade}')

    if quantidade == 60:
        print('Limite de marcações em 1h atingido!\n')
        time.sleep(3600)
        quantidade = 1