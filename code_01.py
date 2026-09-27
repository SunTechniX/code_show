# 15:39
import math

a = float(input())
op = input()
b = float(input())
res = 0
if op == "**":
    res = a ** b
elif op == "*":
    res = a * b
elif op == "-":
    res = a - b
elif op == "+":
    res = a + b
elif op == "/":
    res = a / b
elif op == "%":
    res = b / 100 * a
elif op == "<":
    res = math.sqrt(b)
else:
    print("Операция не определена")
print(f"{a} {op} {b} = {res}")
