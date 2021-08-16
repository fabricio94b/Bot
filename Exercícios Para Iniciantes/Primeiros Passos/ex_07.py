import locale

locale.setlocale(locale.LC_ALL, "pt_br")
# Se o seu windows estiver em português utilize esse código:
# locale.setlocale(locale.LC_ALL, "")

RENDIMENTO = 0.06

saldo_inicial = float(input("Quanto você deseja investir (em reais)? "))

saldo_um_ano = saldo_inicial * (1 + RENDIMENTO)
saldo_dois_anos = saldo_um_ano * (1 + RENDIMENTO)
saldo_três_anos = saldo_dois_anos * (1 + RENDIMENTO)
saldo_quatro_anos = saldo_três_anos * (1 + RENDIMENTO)
saldo_cinco_anos = saldo_quatro_anos * (1 + RENDIMENTO)

print(f"Saldo após um ano: {locale.currency(saldo_um_ano, grouping=True)}")
print(f"Saldo após dois anos: {locale.currency(saldo_dois_anos, grouping=True)}")
print(f"Saldo após três anos: {locale.currency(saldo_três_anos, grouping=True)}")
print(f"Saldo após quatro anos: {locale.currency(saldo_quatro_anos, grouping=True)}")
print(f"Saldo após cinco anos: {locale.currency(saldo_cinco_anos, grouping=True)}")
