from Conversor import f
from Conversor import c


# Conversor de Temperatura

while True:
    # Apresentação
    print('\n\t\t-- Conversor de Temperatura --\n\t')

    # Menu
    print('1. ºC para ºF')
    print('2. ºF para ºC')
    print('3. Sair')

    # Ler a opção de escolha
    op = int(input('\n\tOpção: '))

    if op ==1:
        print('\nºC para ºF\n')

        #Entrada
        n1 = float(input('Informe uma temperatura: '))

        #Processamento
        total = f(n1)

        #Saída
        print(f' {n1}ºC é {total}ºF')

    elif op ==2:
        print('\nºF para ºC\n')

        #Entrada
        n1 = float(input('Informe uma temperatura: '))

        #Processamento
        total = c(n1)

        #Saída
        print(f' {n1}ºF é {total}ºC')

    elif op ==3:
        print('Bye Bye')
        break

    else:
        #Tratamento de exceção
        print(f'\nOpção {op} incorreta!\n')