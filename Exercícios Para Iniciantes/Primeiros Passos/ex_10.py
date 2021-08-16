SEGUNDOS_EM_UM_MINUTO = 60
SEGUNDOS_EM_UMA_HORA = SEGUNDOS_EM_UM_MINUTO * 60
SEGUNDOS_EM_UM_DIA = SEGUNDOS_EM_UMA_HORA * 24

dias = int(input("Informe a quantidade de dias: "))
horas = int(input("Informe a quantidade de horas: "))
minutos = int(input("Informe a quantidade de minutos: "))

segundos = (
    dias * SEGUNDOS_EM_UM_DIA
    + horas * SEGUNDOS_EM_UMA_HORA
    + minutos * SEGUNDOS_EM_UM_MINUTO
)

print(
    (
        f"Em {dias} dia(s), {horas} hora(s) e {minutos} minuto(s) "
        f"temos {segundos} segundo(s)."
    )
)
