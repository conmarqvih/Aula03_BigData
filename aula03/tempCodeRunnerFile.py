pontos = int(input('Informe seus pontos: '))
if pontos >= 100:
    total = pontos + 10
    print(f'Excelente! Agora você têm {total} pontos')

elif pontos >= 50:
    total = pontos + 5
    print(f'Bom desempenho. Você têm {pontos} pontos')

else:
    print(f'Treine mais. Pontação {pontos} pontos')

print('Fim!')