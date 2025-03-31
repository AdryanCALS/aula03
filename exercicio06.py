time1 = input("Digite o nome do primeiro time: ")
time2 = input("Digite o nome do segundo time: ")
gols1 = int(input("Quantos gols o time 1 fez? "))
gols2 = int(input("Quantos gols o time 2 fez? "))
if gols1>gols2:
    print(f"O time vencedor foi {time1}, com {gols1} gols")
else:
    if gols1 == gols2:
        print("Empate!!")
    else:
        print(f"O time vencedor foi {time2}, com {gols2} gols")