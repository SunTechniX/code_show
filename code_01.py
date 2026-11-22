#совместимость 10.0
method Line(Sym: String, n: Number): String
    var line = ""
    for i = 1 to n
        line += Sym
    ;
    return line
;

method Logo(Sym: String, a: Number, b: Number)
    var line = Line(Sym, a)
    Console.Write(line)
    var probel = Line(" ", a - 2)
    for k = 1 to b - 2
        Console.Write(Sym + probel + Sym)
    ;
    Console.Write(line)
;

method Script()
    Logo("*", 7, 5)
    Logo("#", 5, 4)
    Logo("+", 3, 5)
;
