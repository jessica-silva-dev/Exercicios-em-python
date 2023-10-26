# Calculando descontos 
# Faça um algoritmo que leia o preço do produto e mostre o seu novo preço com o desconto.

produto = float(input("Valor do produto: R$"))
desconto =int(input("Desconto recebido: "))
valor = produto - (produto * desconto/100)
print(f"O valor do seu produto é R${produto:.2f}")
print(f"Mas com o desconto de {desconto}% ficou: R${valor:.2f}")