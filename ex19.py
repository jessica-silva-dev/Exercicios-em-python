# Seno, Cosseno e Tangente
from math import sin, cos, radians, tan

angulo = float(input("Informe o ângulo desejado: "))
seno = sin(radians(angulo))
cossemo = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f"O ângulo de {angulo} tem o Seno de: {seno:.2f}")
print(f"O ângulo de {angulo} tem o Cosseno de: {cossemo:.2f}")
print(f"O ângulo de {angulo} tem a Tangente de: {tangente:.2f}")
