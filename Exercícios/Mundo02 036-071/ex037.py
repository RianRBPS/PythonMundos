#Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.


número = int(input('Digite um número inteiro: '))
opção = int(input('Escolha uma das opções de conversão:'
            '\n[ 1 ] converter para BINÁRIO'
            '\n[ 2 ] converter para OCTAL'
            '\n[ 3 ] converter para HEXADECIMAL'
            '\nSua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual à {}'.format(número, bin(número)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual à {}'.format(número, oct(número)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual à {}'.format(número, hex(número)[2:]))
else:
    print('Opção inválida. Tente novamente.')
