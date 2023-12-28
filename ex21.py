from random import shuffle

# Solicita ao usuário a quantidade de nomes a serem ordenados
vezes = int(input("Quantos nomes vai ser ordenados? "))

# Lista vazia para armazenar os nomes
lista = []

# Obtendo os nomes do usuário e adicionando a lista
for i in range(vezes):
    nomes = input(f"Informe o {i+1}° nome: ")
    lista.append(nomes)

# # mudando a ordem dos nomes na lista
shuffle(lista)

# Imprimindo a ordem dos nomes
print(f"A ordem dos nomes será:")
for ordem, nome in enumerate(lista, 1):
    print(f"O {ordem}° nome é: {nome}")