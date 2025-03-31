#Exercicio 1
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite o seu salario: "))
aumento = float(input("Digite a porcentagem do seu aumento: "))
salarioaumento = salario*(aumento/100)+salario
print(f"Ola {nome}, voce tem {idade} anos e seu salario é de: {salario}")
print(f"Seu salario apos o aumento é de: {salarioaumento}")

