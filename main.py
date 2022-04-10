def culc(l):
    S,V,t,V0,a = l

    formuls = [
            [S, "*", (V, t)],
            [V, "+", (V0,("*", (a, t)))],
            [S, "+", ( ("*", (V0, t)) , ("/", (("*", (("**",(t,2)), a)), 2 )) )]
               ]

    var_formuls = [[S, V, t],
                   [V, V0, a, t],
                   [S, V0, t, a]]

    unknowns = [[0,0],
                [0,0],
                [0,0]]

    for i in range(len(var_formuls)):
        unknowns[i][0] = var_formuls[i].count("?")
        unknowns[i][1] = var_formuls[i].count("!")

    for i in range(len(formuls)):
        if unknowns[i][0] == 0 and unknowns[i][1] == 1:
            return rasp(formuls[i])




def rasp(l):
    if type(l)==list:

        z = l[1]
        if  type(l[2][1]) == int:
            if z == "*":
                return l[2][0]*l[2][1]
            if z == "+":
                return l[2][0]+l[2][1]
            if z == "/":
                return l[2][0]/l[2][1]
            if z == "-":
                return l[2][0]-l[2][1]
            if z == "**":
                return l[2][0]**l[2][1]
        elif type(l[2][0]) != tuple:
            if z == "+":
                return l[2][0]+rasp(l[2][1])
            if z == "*":
                return l[2][0]*rasp(l[2][1])
            if z == "/":
                return l[2][0]/rasp(l[2][1])
            if z == "-":
                return l[2][0]-rasp(l[2][1])
            if z == "**":
                return l[2][0]**rasp(l[2][1])
        else:
            if z == "+":
                return rasp(l[2][0])+rasp(l[2][1])
            if z == "*":
                return rasp(l[2][0])*rasp(l[2][1])
            if z == "/":
                return rasp(l[2][0])/rasp(l[2][1])
            if z == "-":
                return rasp(l[2][0])-rasp(l[2][1])
            if z == "**":
                return rasp(l[2][0])**rasp(l[2][1])

    else:
        if type(l[1][0]) != tuple:
            z = l[0]
            if z == "*":
                return l[1][0]*l[1][1]
            if z == "+":
                return l[1][0]+l[1][1]
            if z == "-":
                return l[1][0]-l[1][1]
            if z == "/":
                return l[1][0]/l[1][1]
            if z == "**":
                return l[1][0]**l[1][1]
        else:
            z = l[0]
            if z == "*":
                return rasp(l[1][0]) * l[1][1]
            if z == "+":
                return rasp(l[1][0]) + l[1][1]
            if z == "-":
                return rasp(l[1][0]) - l[1][1]
            if z == "/":
                return rasp(l[1][0]) / l[1][1]
            if z == "**":
                return rasp(l[1][0]) ** l[1][1]





S = "!"
V = "?"
t = 5
V0 = 5
a = 5


f = culc((S, V, t, V0, a))
print(f)
