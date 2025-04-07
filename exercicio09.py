hora1 = int(input("Digite a hora 1: "))
minuto1 = int(input("Digite o minuto 1: "))
hora2 = int(input("Digite a hora 2: "))
minuto2 = int(input("Digite o minuto 2: "))
minutosaida = minuto2+minuto1
horasaida = hora1+hora2

if horasaida > 12 and horasaida <= 24:
    horasaida = horasaida -12
elif horasaida > 24 and horasaida < 36:
    horasaida = horasaida-24
elif horasaida >= 36:
    horasaida = horasaida-36
else:
    horasaida = horasaida - 48

if minutosaida >= 60:
    horasaida += 1
    minutosaida = minutosaida-60

    print(f"{horasaida}:{minutosaida}")
else:
    print(f"{horasaida}:{minutosaida}")