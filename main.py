import time
from metodos import Bot

marcacoes = input('Digite a lista de @ que deseja marcar: ').split()
quantidade = int(input('Quantidade de @ que deseja marcar (máx 4): '))

obj = Bot(marcacoes, quantidade)

tempo = int(input('Tempo de espera entre as marcações (recomendado 60): '))

quantidade = 0
time.sleep(5)

while True:
    obj.comentar()
    time.sleep(tempo)
    quantidade += 1
    print(f'Quantidade de marcações já feitas: {quantidade}')
    if quantidade == 60:
        print('Limite de marcações em 1h atingido!')
        time.sleep(3600)
        quantidade = 0