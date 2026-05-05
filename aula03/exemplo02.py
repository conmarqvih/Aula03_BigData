# idade = int(input('Digite a idade: '))  # 19 

 # > <, >=(maior igual), <=(menor igual), ==(igual), !=(diferente)


# if idade >= 18:
 #   print('Você é adulto')
# else: 
 #   print('Você é menor de idade')

#-------------------------------------------------

 # Classificação por Pontos (> 100 - 10 | >50 - 5 | <50 0) | IF (SE), Elif (SE NÃO), ELSE (CASO CONTRÁRIO)

pontos = int(input('Informe seus pontos: '))
if pontos >= 100:
    total = pontos + 10
    print(f'Excelente! Agora você têm {total} pontos')

elif pontos >= 50:
    total = pontos + 5
    print(f'Bom desempenho. Você têm {pontos} pontos')

else:
    print(f'Treine mais. Pontuação {pontos} pontos')

print('Fim!')