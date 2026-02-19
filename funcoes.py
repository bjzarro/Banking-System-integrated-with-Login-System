from datetime import datetime

def depositar(archive):
    # função de depósito
    datenow = datetime.now()
    operation_date = datenow.strftime('%d/%m/%Y %H:%M:%S')
    print('Digite o valor a ser depositado')
    value = float(input('>'))
    archive.write(f'1,{value},{operation_date}\n')
    print(f'Depósito de R${value:.2} realizado com sucesso.')

def saque(archive):
    # função de saque
    datenow = datetime.now()
    operation_date = datenow.strftime('%d/%m/%Y %H:%M:%S')
    print('Digite o valor a ser sacado')
    value = float(input('>'))
    total = saldo(archive)
    if value > total:
        print('Saldo insuficiente para operação.')
    else:
        archive.write(f'2,{value},{operation_date}\n')
        print(f'Saque de R${value:.2} realizado com sucesso.')

def saldo(archive):
    # função de exibir saldo
    archive.seek(0)
    lines = archive.readlines()
    total = 0
    for i in lines:
        if i.startswith('1'):
            value = float(i.split(',')[1].split(',')[0])
            total += value
        elif i.startswith('2'):
            value = float(i.split(',')[1].split(',')[0])
            total -= value
        else:
            break
    return total

def extrato(archive):
    # função de imprimir extrato
    archive.seek(0)
    lines = archive.readlines()
    for i in lines:
        tipo,value,data = i.strip().split(',')
        if tipo == '1':
            operation = 'Depósito'
        elif tipo == '2':
            operation = 'Saque'
        else:
            operation = 0
        print(f'{operation:<10} | {value:>10} | {data}')