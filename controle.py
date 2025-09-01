presencas = {
    "segunda": {"Ana", "Bruno", "Carla", "Diego"},
    "terca":   {"Ana", "Bruno", "Carla"},
    "quarta":  {"Ana", "Bruno", "Diego"},
    "quinta":  {"Ana", "Carla", "Diego"},
    "sexta":   {"Ana", "Bruno", "Carla", "Diego"},
}

dias = list(presencas.keys())

presentes_todos_os_dias = set(presencas[dias[0]])
for d in dias[1:]:
    presentes_todos_os_dias &= presencas[d]

presentes_algum_dia = set()
for s in presencas.values():
    presentes_algum_dia |= s

faltaram_algum_dia = presentes_algum_dia - presentes_todos_os_dias

contagem_presencas = {}
for s in presencas.values():
    for a in s:
        contagem_presencas[a] = contagem_presencas.get(a, 0) + 1

while True:
    opcao = input("\nDigite (1) todos os dias, (2) faltaram, (3) total, (0) sair: ")
    if opcao == "1":
        print("Presentes todos os dias:", presentes_todos_os_dias)
    elif opcao == "2":
        print("Faltaram em pelo menos um dia:", faltaram_algum_dia)
    elif opcao == "3":
        print("Total de presenças por aluno:", contagem_presencas)
    elif opcao == "0":
        break
    else:
        print("Opção inválida.")