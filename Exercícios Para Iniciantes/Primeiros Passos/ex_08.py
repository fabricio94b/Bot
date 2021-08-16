import math

DOSE_DIÁRIA = 1.6
TOTAL_NO_FRASCO = 20.0
DIAS_EM_UM_MÊS = 30.5

meses_de_tratamento = int(input("O tratamento vai durar quantos meses? "))

dias_de_tratamento = DIAS_EM_UM_MÊS * meses_de_tratamento
caixas_a_comprar = math.ceil(DOSE_DIÁRIA * dias_de_tratamento / TOTAL_NO_FRASCO)

print(f"Você deve comprar {caixas_a_comprar} caixas de remédio.")
