base_maior = float(input("Insira o valor de uma das bases do trapézio em metros: "))
base_menor = float(input("Insira o valor da outra base do trapézio em metros: "))
altura = float(input("Insira o valor da altura do trapézio em metros: "))

área = (base_maior + base_menor) * altura / 2

print(f"A área do trapézio mede {área:.2f}m².")
