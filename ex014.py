# Reajuste salarial

salario = float(input("Qual é o valor do seu salário? R$"))
desc = int(input("Porcentagem do reajuste salarial recebido: "))
total = salario + (salario*desc/100)

print(f"Seu sálario era de: R${salario}")
print(f"Agora com o reajuste recebido de {desc}%")
print(f"Parabéns! Você passa a receber: R${total:.2f}")