# Faça um algoritimo que leia o valor do produto, se for pago a vista ganha desconto.
# Se for parcelado tem um acrescimo.

produto = float(input("Informe o valor da compra do produto: R$ "))
vista = input("O pagamento é a vista? ")
print('')
if vista.lower() == "sim" or vista.lower() == "s":
    desc = produto - (produto * 10/100)
    print(f"Otima escolha! O valor do compra era: {produto:.2f}\nMas como você efetuou o pagamento a vista!\nSeu valor com desconto é: {desc:.2f}")
elif vista.lower() == "não" or vista.lower() == "nao":
    desc1 = produto + (produto * 10/100)
    print(f"O valor do compra era: {produto:.2f}\nMas como você efetuou o pagamento parcelado!\nSeu valor da compra com o juros é: {desc1:.2f}")
else:
    print("Nao reconhecemos essa forma de pagamento!")