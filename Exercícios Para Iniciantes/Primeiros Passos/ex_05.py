import locale

locale.setlocale(locale.LC_ALL, "pt_br")
# Se o seu windows estiver em português utilize esse código:
# locale.setlocale(locale.LC_ALL, "")

TAXA_AUMENTO = 0.05
TAXA_BÔNUS = 0.2
MESES_DE_TRABALHO = 12

salario_atual = float(input("Insira o seu salário: "))

novo_salario = salario_atual * (1 + TAXA_AUMENTO)
bônus_fim_de_ano = novo_salario * TAXA_BÔNUS
total_recebido = novo_salario * MESES_DE_TRABALHO + bônus_fim_de_ano

print(f"O seu novo salário é {locale.currency(novo_salario, grouping=True)}.")
print(f"O seu bônus será de {locale.currency(bônus_fim_de_ano, grouping=True)}.")
print(
    (
        f"Em {MESES_DE_TRABALHO} meses de trabalho você receberá "
        f"{locale.currency(total_recebido, grouping=True)} em salários e bônus."
    )
)
