hora = int(input("Digite um horário:"))
if hora < 0 or hora > 23:
    print("Digite um número entre 0 e 23")
else:
    if  4 < hora < 12:
        print("Está de manhã")
    elif 11 < hora < 18:
        print("Está de tarde")
    else:
        print("Está de noite")

