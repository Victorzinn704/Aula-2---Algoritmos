emprestimos = [
    ["Batman", "Ana", 5],
    ["Coringa", "Pedro", 12],
    ["O Hobbit", "Marina", 3],
    ["Harry Potter", "João", 9]
]

def listar_mais_7():
    mais_7 = [item for item in emprestimos if item[2] > 7]
    if mais_7:
        print("\nLivros emprestados há mais de 7 dias:")
        for t, u, d in mais_7:
            print(f"- {t}, com {u}, há {d} dias")
    else:
        print("\nNenhum livro há mais de 7 dias.")

def listar_mais_tempo():
    if emprestimos:
        t, u, d = max(emprestimos, key=lambda x: x[2])
        print(f"\nLivro emprestado há mais tempo: {t}, com {u}, há {d} dias")
    else:
        print("\nNenhum empréstimo registrado.")

def listar_usuarios():
    usuarios = sorted(set(u for _, u, _ in emprestimos))
    print("\nUsuários com livros emprestados:", ", ".join(usuarios))

def mostrar_media():
    if emprestimos:
        media = sum(d for _, _, d in emprestimos) / len(emprestimos)
        print(f"\nMédia de dias de empréstimo: {media:.1f}")
    else:
        print("\nNenhum empréstimo registrado.")

while True:
    print("\n=== Sistema de Biblioteca ===")
    print("1) Livros emprestados há mais de 7 dias")
    print("2) Livro emprestado há mais tempo")
    print("3) Usuários com livros emprestados")
    print("4) Média de dias de empréstimo")
    print("0) Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        listar_mais_7()
    elif opcao == "2":
        listar_mais_tempo()
    elif opcao == "3":
        listar_usuarios()
    elif opcao == "4":
        mostrar_media()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")