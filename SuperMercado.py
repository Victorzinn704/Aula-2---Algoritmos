estoque = [
    ["Arroz", 10, 5.50],
    ["Feijao", 3, 8.20],
    ["Macarrao", 12, 4.00],
    ["Acucar", 2, 3.70],
    ["Cafe", 7, 15.00]
]

valor_total = sum(qtd * preco for _, qtd, preco in estoque)
print(f"Valor total em estoque: {valor_total:.2f}")

produto_maior = max(estoque, key=lambda x: x[1] * x[2])
print(f"Produto de maior valor total: {produto_maior[0]} (qtd={produto_maior[1]}, preço={produto_maior[2]:.2f}, total={produto_maior[1]*produto_maior[2]:.2f})")

baixo_estoque = [nome for nome, qtd, _ in estoque if qtd < 5]
print("Produtos com menos de 5 unidades:", baixo_estoque if baixo_estoque else "Nenhum")

nome_busca = input("Digite o nome do produto para buscar: ").strip().lower()
encontrado = next((item for item in estoque if item[0].lower() == nome_busca), None)

if encontrado:
    n, q, p = encontrado
    print(f"Produto encontrado: {n} | qtd={q} | preço={p:.2f} | total={q*p:.2f}")
else:
    print("Produto não encontrado.")
