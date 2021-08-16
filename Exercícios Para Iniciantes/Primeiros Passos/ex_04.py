import locale

locale.setlocale(locale.LC_ALL, "pt_br")
# Se o seu windows estiver em português utilize esse código:
# locale.setlocale(locale.LC_ALL, "")

PREÇO_PASTEL = 8.0
PREÇO_REFRIGERANTE = 5.0

quantidade_pastéis = int(input("Quantos pastéis você deseja? "))
quantidade_refrigerantes = int(input("Quantos refrigerantes você deseja? "))

preço_do_pedido = (
    quantidade_pastéis * PREÇO_PASTEL + quantidade_refrigerantes * PREÇO_REFRIGERANTE
)

preço_do_pedido_em_reais = locale.currency(preço_do_pedido, grouping=True)

print(f"O total do seu pedido é {preço_do_pedido_em_reais}.")
