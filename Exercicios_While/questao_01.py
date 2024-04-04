numero = int(input("Digite um número inteiro para ver sua tabuada: "))

multiplicador = 0


print(f"Tabuada do {numero}:")

while multiplicador <= 10:
    resultado = numero * multiplicador

    print(f"{numero} x {multiplicador} = {resultado}")
    
    multiplicador += 1