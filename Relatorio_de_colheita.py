print("Insira as toneladas colhidas por mês")
meses = []
for i in range(12):
    mes = float(input(f"Mês {i+1}:"))
    manual = round(mes * 0.05, 5)  # Calcula a perda manual no mês
    print("Perda manual: " + str(manual))
    maquina = round(mes * 0.15, 5)  # Calcula a perda por máquina no mês
    print("Perda por máquina: " + str(maquina))
    meses.append(mes)

total = sum(meses)  # Soma a colheita total no ano
perda1 = sum(meses) * 0.05  # Calcula a perda manual no ano
perda2 = sum(meses) * 0.15  # Calcula a perda com máquina no ano

print("\nRELATÓRIO CONSOLIDADO: ")
print("\nColheita do ano: " + str(total) + " Toneladas")
print("\nProjeção de desperdício: ")
print("Manual: " + str(perda1) + " Toneladas")
print("Com Máquina: " + str(perda2) + " Toneladas")
input("\nPressione 'Enter' para sair")

