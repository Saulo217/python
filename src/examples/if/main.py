nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media > 6:
    print(f"O aluno {nome}, está aprovado, média = {media:.2f}")
elif media >= 2 and media <= 6:
    print(f"O aluno {nome}, está de exame, média = {media:.2f}")
else:
    print(f"O aluno {nome}, está reprovado, média = {media:.2f}")
