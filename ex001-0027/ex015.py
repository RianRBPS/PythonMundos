#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos kms foram rodados?'))
dias = int(input('Por quantos dias o carro foi alugado? '))
pago = (dias * 60) + (km * 0.15)
print('O valor a ser pago será R${:.2f}'.format(pago))