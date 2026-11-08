from random import choice

print("Игра 'Камень, Ножницы, Бумага'")
# К > Н > Б > К ...
KNB = ("К", "Н", "Б")
me, pk = 0, 0
a = input().upper()
while a != "Х" and a != "X":
    if a not in KNB:
        print("Ты сделал неправильный ввод")
        exit(0)
    b = choice(KNB)
    print(a, b)
    if a == b:
        print("Ничья")
    elif (a == "К" and b == "Н") \
            or (a == "Н" and b == "Б") \
            or (a == "Б" and b == "К"):
        print("Я выиграл!")
        me += 1
    else:
        print("ПК выиграл!")
        pk += 1
    a = input().upper()

print(f"Счёт: Я: {me} | ПК: {pk}")
