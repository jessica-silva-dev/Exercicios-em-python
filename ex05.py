# Faça um programa que leia um número inteiro, e mostre na tela o seu antecessor e seu sucessor.

# informação para o usuário

print('-------> PRIMEIRO EXERCÍCIO <-------')

# Laço de repetição
for i in range(0, 3):

# Entrada do usuário
    num = int(input('Digite um número: '))

# Variáveis para antecessor e sucessor

    sucessor = num +1
    antecessor = num -1

    print(f'Seu número é = {num}')
    print(f'O antecessor é = {antecessor}')
    print(f'O sucessor é = {sucessor}') 

# Informação para o usuário

print('-------> PROXÍMO EXERCÍCIO <-------')
    
# Faça um programa que leia um número, e que mostre na tela qual é o dobro, o triplo e a raiz quadrado desse número.

# Laço de repetição

for resultado in range(0, 3):
    num1 = int(input('Digite um número: '))
    dobro = num1 + num1
    triplo = num1 * 3
    raiz = num1 **(1/2)
    print(f'O valor escolhido foi: {num1}')
    print(f'O dobro de {num1} é: {dobro}')
    print(f'O triplo de {num1} é:  {triplo}')
    print(f'A raiz quadrada de {num1} é : {raiz}')
