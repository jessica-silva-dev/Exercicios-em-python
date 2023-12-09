# Quebrando um número
import random
from time import sleep
from math import trunc
sleep(2)
repetir = int(input("Quantas vezes quer repetir o programa? "))
sleep(2)
for i in range(repetir):
    numero = float(input("Informe um número real: "))
    sleep(1)
    print(f"O valor digitado foi de {numero} e sua porção inteira é: {trunc(numero)}")
    sleep(2)
print("")
sleep(3)
print("-" * 75)
print("Outra maneira!\nAgora com números aleatórios da biblioteca random.")
print("-" * 75)
sleep(4)
repetir1 = int(input("Quantas vezes quer repetir o programa? "))
for j in range(repetir1):
    valor_aleatorio = random.uniform(1.0, 50.0)
    sleep(1)
    print(f"O número aleatótio foi {valor_aleatorio}, e em número inteiro é: {int(valor_aleatorio)}")
    sleep(3)
