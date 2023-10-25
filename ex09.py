# Conversur de moedas

# Crie um programa que leia quanto o usuário tem na carteira, e converta o valor em dólares.
# Dolar = US$ 1.00
# Real = R$ 4.99

valor = float(input("Quanto você tem na sua carteira? R$"))

dolar =  valor / 4.99
euro = valor / 5.29
peso_arg = valor / 0.014
yuan = valor / 0.68
libra = valor / 6.06
franco = valor / 5.58


print(f"Você tem: R$ {valor}")
print(f"Em Dolar é: US$ {dolar:.2f}")
print(f"Em Euro é: EUR {euro:.2f}")
print(f"Em Peso Arg é: ARG {peso_arg:.2f}")
print(f"Em Yuan Chinês é: CNY {yuan:.2f}")
print(f"Em Libra Esterlina é: GPB {libra:.2f}")
print(f"Em Franco Suíço é: CHF {franco:.2f}")