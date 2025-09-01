vendas = [10, 15, 20, 5, 0, 8, 25, 30, 12, 18, 22, 5, 9, 14, 16, 28, 10, 7, 19, 11]

total = sum(vendas)
print("Total de vendas no mês:", total)

maior = max(vendas)
menor = min(vendas)
print("Dia com mais vendas:", vendas.index(maior)+1, "(", maior, ")")
print("Dia com menos vendas:", vendas.index(menor)+1, "(", menor, ")")

media = total / len(vendas)
print("Média de vendas por dia:", media)

acima_media = [i+1 for i, v in enumerate(vendas) if v > media]
print("Dias com vendas acima da média:", acima_media)