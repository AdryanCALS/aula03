nota1 = float(input("Digite a nota 1 do aluno: "))
nota2 = float(input("Digite a nota 2 do aluno: "))
nota3 = float(input("Digite a nota 3 do aluno: "))
media = (nota3+nota2+nota1)/3
if media >= 7:
    print(f"Aluno aprovado com media {media:.2f}")
if media < 4:
    print(f"Aluno reprovado com media {media:.2f}")
else:
    print(f"Aluno em recuperação com media {media:.2f}")