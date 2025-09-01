palestra = ["Ana", "Carlos", "Marina"]
workshop = ["Carlos", "João", "Ana"]
mesa_redonda = ["Marina", "João", "Paula"]

todos = [set(palestra), set(workshop), set(mesa_redonda)]

participaram_todas = set.intersection(*todos)
print("Participaram de todas as atividades:", participaram_todas)

participaram_uma = [p for lista in todos for p in lista
                    if sum(p in s for s in todos) == 1]
print("Participaram de apenas uma atividade:", set(participaram_uma))

nomes_unicos = set.union(*todos)
print("Todos os nomes únicos:", nomes_unicos)

print("Número de participantes distintos:", len(nomes_unicos))
print("Número total de participações (contando repetições):", sum(len(s) for s in todos))