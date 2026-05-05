# Exercício 01
#-----------------------

valor = int(input('Informe o valor da compra: R$ '))
if valor > 250:
    desconto = valor * 0.16
    total_desconto = valor - desconto
    print(f'Você ganhou 16% de DESCONTO. Valor total: R$ {total_desconto}.')

else:
    print(f'O valor total da compra é de: R$ {valor}')


print('Obriga por comprar conosco. Volte sempre!')