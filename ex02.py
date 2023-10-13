# PRATICANDO COM AS CONDICIONAIS


# Encontrar o maior número entre os valores

# Entrada de dados do usuário

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

# Condição a ser seguida:

if valor1 > valor2:
  print(f'O maior valor é {valor1}')
elif valor1 < valor2:
  print(f'O maior valor é {valor2}')
else:
  print("Os valores são iguais")