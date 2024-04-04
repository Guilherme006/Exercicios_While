N = int(input("Digite um número inteiro para calcular o somatório dos N primeiros números inteiros: "))

somatorio = 0
numero = 1


while numero <= N:
    
    somatorio += numero
    numero += 1
   


print("O somatório dos", N, "primeiros números inteiros é:", somatorio)