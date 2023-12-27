# Cateto e Hipotenusa
from math import hypot

cateto_oposto = float(input("Informe o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Informe o comprimento do cateto adjacente: "))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/5)

print(f"A hipotenusa de {cateto_oposto} e {cateto_adjacente} é: {hipotenusa:.4f}")

# Outra maneira usando a biblioteca math

"""
cateto_opt = float(input("Informe o comprimento do cateto oposto: "))
cateto_adj = float(input("Informe o comprimento do cateto adjacente: "))
hipotenusa = hypot(cateto_opt, cateto_adj)

print(f"A hipotenusa de {cateto_opt} e {cateto_adj} é: {hipotenusa:.4f}")
"""