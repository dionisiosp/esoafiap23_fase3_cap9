# Nome: Dionisio Sant'Ana Pereira
# RM: 97985

print("Insira as toneladas colhidas por mês:")
print("")
print("")

mes = 1
tmanual = 0
tmaquina = 0
colheita = 0

while mes <= 12:
    tonelada = input()
    
    while not tonelada.isdigit():
        print("A entrada deve ser um número em toneladas!")
        print("Insira NOVAMENTE as toneladas colhidas por mês:")
        print("")
        tonelada = input()
    
    print("Mês", mes, "....:",tonelada)
    manual = int(tonelada) * 0.05
    maquina = int(tonelada) * 0.15
    print(f'     Perda manual..........: {manual:,.2f}')
    print(f'     Perda com máquina.....: {maquina:,.2f}')
    print("")
    mes = mes + 1
    tmanual = tmanual + manual
    tmaquina = tmaquina + maquina
    colheita = colheita + int(tonelada)

print("")
print("RELATÓRIO CONSOLIDADO:")
print("")
print("")
print(f'Colheita do ano.....: {colheita:,.2f} Toneladas')
print("Projeção de desperdício:")
print(f'  Manual..........: {tmanual:,.2f}')
print(f'  Com máquina.....: {tmaquina:,.2f}')
