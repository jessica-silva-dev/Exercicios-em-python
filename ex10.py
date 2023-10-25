# Resolvendo equação de segundo grau usando vetor e append

# Fórmula da equação de segundo grau
# ax^2 + bx + c = 0
# delta = b^2 - 4 * a * c
# x = (-b - raiz(delta)) / (2 * a)
# x = (-b + raiz(delta)) / (2 * a)

# Declarando um vetor vazio

vetor = []  

# Entrada do usuário

a = int(input("Digite o valor do coeficiente a: "))
b = int(input("Digite o valor do coeficiente b: "))
c = int(input("Digite o valor do coeficiente c: "))

# Adiciomamdo o valor da variável a, b e c ao meu vetor, chamado vetor.

vetor.append(a)
vetor.append(b)
vetor.append(c)

# Exibindo o tamanho/quantidade do meu vetor

print(len(vetor))

# Exibindo os valores de a, b e c adicionados ao vetor.
# Obs: começa pela posição 0 

print(vetor[0])
print(vetor[1])
print(vetor[2])

# Usando o vetor na equação
# delta = b^2 - 4 * a * c

delta = vetor[1]**2 - 4 * vetor[0] * vetor[2]

# x = (-b - raiz(delta)) / (2 * a)

x1 = (-vetor[1] - delta**0.5) / (2 * vetor[0])

# x = (-b + raiz(delta)) / (2 * a)

x2 = (-vetor[1] + delta**0.5) / (2 * vetor[0])

print("O valor de delta é : ", delta)
print("O valor de x1 é : ", x1)
print("O valor de x2 é : ", x2)