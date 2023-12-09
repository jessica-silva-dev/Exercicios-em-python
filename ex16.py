# Aluguel de carros

# Entrada de dados
km = float(input("Informe a quantidade de km rodados: "))
dias = int(input("Informe quantos dias o carro ficou alugado? "))
aluguel = float(input("Informe qual o valor do aluguel por dia? "))
km_rodados = float(input("Informe qual o valor de cada km rodados "))
# Resolução
valor_km = km * km_rodados
valor_aluguel = dias * aluguel
valor_total = valor_km + valor_aluguel

# Exibindo o resultado para o usuario
print(f"No total de {dias} dias de carro alugado, o valor a ser pago é de: {valor_aluguel:.2f}")
print(f"E como teve {km:.2f} km utilizado no carro, ficou mais um acréscimo de: {valor_km:.2f}")
print(f"Portanto o valor total a ser pago é de: {valor_total:.2f}")


