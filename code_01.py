#        012345
line1 = "╔╗╚╝║═"
line2 = "┌┐└┘│─"
line3 = "╭╮╰╯│─"

def logo(name, syms):
    n = len(name)
    line = syms[5] * (n + 2)
    print(f"{syms[0]}{line}{syms[1]}")
    print(f"{syms[4]} {name} {syms[4]}")
    print(f"{syms[2]}{line}{syms[3]}")

# ПРОГРАММА НАЧИНАЕТСЯ ЗДЕСЬ!
logo("Роман", line3)
logo("Александр", line2)
