nota_valida = False

while not nota_valida:
    nota = int(input("Digite sua nota: "))

    if nota <= 7:
        nota_valida = False
    else:
        nota_valida = True
        print("Parabens, voce passou!")
        break
    
    