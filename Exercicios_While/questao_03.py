soma = 0
quantidade = 0

leitura_numero = False

 

while not leitura_numero:
    numero = int(input("Digite um número inteiro ou digite -1 para encerrar: "))
    
    soma += numero
    quantidade += 1


    if numero != -1:
       numero = int(input("Digite um número inteiro ou digite -1 para encerrar: "))

       media = soma / quantidade
    else:
       print("A média dos números é", media)
       break
