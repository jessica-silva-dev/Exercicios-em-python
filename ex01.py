# PRATICANDO COM AS CONDICIONAIS

# Se um aluno chegar atrasado na sala de aula mais de 3 vezes, ele vai levar uma suspensão.

# Entrada de dados para o aluno informar a quantidade de vezes que chegou atrasado.
 
vezes_atrasada = int(input("Quantas vezes você chegou atrasado?  "))

if vezes_atrasada > 3:
  print("Você está suspenso!")
else:
  print("Você pode entrar!")