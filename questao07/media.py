nome = input("Digite seu nome:")
disciplina = input("Digite a disciplina:")
n1 = int(input("Digite n1:"))
n2 = int(input("Digite n2:"))
m = (n1 + n2)/2
if m >=6:
    print(f'{nome}, você está aprovado na disciplina de {disciplina}')
else:
    print(f'{nome}, você está reprovado na disciplina de {disciplina}')
    