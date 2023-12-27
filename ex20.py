import random
repetir = int(input("Informe a quantidade de nomes que vai ser sorteado: "))
lista = []
for i in range(repetir):
     nome = input(f"Digite o {i+1}° nome: ")
     lista.append(nome)
sorteado = random.choice(lista)
print(f"O nome escolhido foi: {sorteado}")