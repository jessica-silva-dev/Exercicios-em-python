# Faça um programa que leia a nota do aluno, e veja a média se passou ou foi reprovado.

# Laço de repetição

for avaliacao in range(0, 3):
    nota = float(input('Digite um número: '))
    nota1 = float(input('Digite um número: '))
    media = (nota + nota1) / 2
    if media >= 6:
        print(f"Sua média é = {media}")
        print("Parabéns você foi APROVADO!")
    else:
        print(f"Sua média é = {media}")
        print("Estude mais um pouco, você foi REPROVADO!")