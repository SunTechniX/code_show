from random import randint

n = int(input())
for i in range(1, n + 1):
    x = randint(1, n)
    print(f"{i} * {x} = {i * x}")
