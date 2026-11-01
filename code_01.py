def logo(name):
    n = len(name)
    line = "═" * (n + 2)
    print(f"╔{line}╗")
    print(f"║ {name} ║")
    print(f"╚{line}╝")

# ПРОГРАММА НАЧИНАЕТСЯ ЗДЕСЬ!
logo("Роман")
logo("Александр")
