# Escreva um programa que leia o valor em metros, e exiba convertido em várias medidas.

valor = float(input("Digite uma distância em metros: "))

km = valor / 1000
hm = valor * 100
dcam = valor / 10
dcim = valor * 10
cm = valor * 100
mm = valor * 1000

print("Distância em ...")
print(F"Em metros é: {valor}")
print(f"Em quilômetros é: {km:.4f}")
print(f"Em hectômetros é: {hm:.4f}")
print(f"Em decâmetros é: {dcam:.4f}")
print(f"Em decímetros é: {dcim}")
print(f"Em centímetros é: {cm:.2f}")
print(f"Em milímetros é: {mm:.3f}")