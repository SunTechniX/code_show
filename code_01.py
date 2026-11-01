from random import randint

#        012345
line1 = "╔╗╚╝║═"
line2 = "┌┐└┘│─"
line3 = "╭╮╰╯│─"
line4 = "▓▓▓▓▓▓"

def logo(name, mode=0):
    n = len(name)
    if mode == 1:
        syms = line1
    if mode == 2:
        syms = line2
    if mode == 3:
        syms = line3
    else:
        syms = line4
    line = syms[5] * (n + 2)
    print(f"{syms[0]}{line}{syms[1]}")
    print(f"{syms[4]} {name} {syms[4]}")
    print(f"{syms[2]}{line}{syms[3]}")

# ПРОГРАММА НАЧИНАЕТСЯ ЗДЕСЬ!
logo("Роман", randint(1, 4))
logo("Александр", randint(1, 4))
logo("Владислав", randint(1, 4))