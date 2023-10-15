# PRATICANDO COM O FOR - LAÇOS DE REPETIÇÃO

# Criei uma lista com diversos valores

numeros = [0, 45, 6, 5, 400, 78, 56]

# Para cada numero em numeros

for numero in numeros:
    print(numero)
    
# Para cada item ou valor que tiver em numeros(variável da lista) percorra e exiba em numero(variável criada para exibir os valores) cada valor que tem em minha lista

# Posso fazer isso com palavras

nome = "Jessica"

for letra in nome:
    print(letra)

# Para cada letra que tiver no valor nome(variável) exiba cada uma delas

# FOR COM RANGE 

# Pode receber 3 parâmetros (inicio, fim, pular de quantos em quantos)

# Pra cada total(variável criada que vai exibir os valores) de 0(início) a 20(término), pular esses números de 2 em 2.

# No terceiro parâmetro eu coordeno se quero que ele vai para frente ou para trás

# Para puçar para fremte número positivos = 2, 5
# Para trás números negativos = -2, -5, 

for total in range(0, 20 + 1, 2):
    print(total)
    
    
        

