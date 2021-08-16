SEGUNDOS_EM_UM_MINUTO = 60
SEGUNDOS_EM_UMA_HORA = SEGUNDOS_EM_UM_MINUTO * 60
SEGUNDOS_EM_UM_DIA = SEGUNDOS_EM_UMA_HORA * 24

segundos = int(input("Informe a quantidade de segundos: "))

dias = segundos // SEGUNDOS_EM_UM_DIA
resto_segundos = segundos % SEGUNDOS_EM_UM_DIA

horas = resto_segundos // SEGUNDOS_EM_UMA_HORA
resto_segundos = resto_segundos % SEGUNDOS_EM_UMA_HORA

minutos = resto_segundos // SEGUNDOS_EM_UM_MINUTO
resto_segundos = resto_segundos % SEGUNDOS_EM_UM_MINUTO

print(
    (
        f"{segundos} segundo(s) equivale(m) a {dias} dia(s), "
        f"{horas} hora(s), {minutos} minuto(s) e {resto_segundos} segundo(s)."
    )
)
