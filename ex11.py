# Faça um programa que leia a largura e altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que  cada litro de tinta, pinta uma área de 2m quadrados.

altura = float(input("Altura da parede: "))
largura = float(input("Largura da parede: "))
total = largura * altura
tinta = total / 2

print(f"Sua parede tem a dimensão de: {largura}x{altura}")
print(f"E a sua área é de: {total}m²")
print(f"E para pintar a parede você vai precisar de: {tinta} litros de tinta.")
