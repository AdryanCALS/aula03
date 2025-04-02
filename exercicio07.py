litros = float(input("Digite o quantos litros de combustivel foram abastecidos: "))
combustivel = input("Digite o tipo de combustivel que foi abastecido(G-gasolina, E-etanol): ")
gasolina = 5.8
etanol = 4.9

if combustivel == 'g':
    valor = litros*gasolina
    print(f"O valor final foi: RS{valor:.2f}")
elif combustivel == 'e':
    valor = etanol*litros
    print(f"O valor final foi: RS {valor:.2f}")
else:
    print("Digite E ou G!!")