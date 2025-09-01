emprestimos = [
    ["Pequeno Principe", "Maria", 5],
    ["Harry Potter", "Ana", 12],
    ["Batman", "Lohana", 3],
    ["Coringa", "Joao", 9]
]

mais_7 = [item for item in emprestimos if item[2] > 7]
print("Livros emprestados há mais de 7 dias:")
for t, u, d in mais_7:
    print(f"- {t}, com {u}, há {d} dias")

mais_tempo = max(emprestimos, key=lambda x: x[2]) if emprestimos else None
if mais_tempo:
    t, u, d = mais_tempo
    print(f"\nLivro emprestado há mais tempo: {t}, com {u}, há {d} dias")

usuarios = sorted(set(u for _, u, _ in emprestimos))
print("\nUsuários com livros emprestados:", ", ".join(usuarios))

media = sum(d for _, _, d in emprestimos) / len(emprestimos) if emprestimos else 0
print(f"\nMédia de dias de empréstimo: {media:.1f}")