from datetime import datetime
from funcoes import depositar,saque,saldo,extrato

confirmation = input('Pressione ENTER para entrar no banco...')
user = str(input('Usuário:'))
password = str(input('Senha:'))

if user == 'usuario' and password == 'senha':
    with open('extratos.txt','a+', encoding='utf8') as archive:
        while confirmation != 'X':
            date_now = datetime.now()
            new_date2 = date_now.isoformat()
            menu_date = date_now.strftime('%d/%m/%Y %H:%M:%S')
            print(f"""
            |==================================================|
            |                   BIZAR BANK                     |
            |==================================================|
            |==================================================|
            |               {menu_date}                |
            |==================================================|
            1 - Depositar dinheiro na conta.
            2 - Sacar dinheiro.
            3 - Exibir Saldo.
            4 - Imprimir Extrato.
            5 - Sair.""")
            
            while True:
                try:
                    option = int(input('>'))
                    break
                except ValueError:
                    print('Caractere inválido.')
                    print()
                
            if option == 1:
                depositar(archive)

            elif option == 2:
                saque(archive)
            
            elif option == 3:
                saldo(archive)

            elif option == 4:
                extrato(archive)

            elif option == 5:
                print('Loggout realizado com sucesso.')
                break
            
            else:
                print('Opção inválida, selecione uma opção existente.')

else:
    print('Usuário ou senha incorretos.')