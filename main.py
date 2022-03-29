def culc(l):

    for i in range(len(l)):
        if l[i] == "!":
            find = i
            break

    S,V,t,V0,a = l

    formuls = [[S, "*", (V, t)],
               [V, "+", (V0,("*", (a, t)))],
               [S, "+", ( ("*", (V0, t)) , ("/", ("*", (a, ("**",t) ) ) ,(2) ) )]]
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
    if type(l[1]) == "str":
        z = l[1]
        if tuple() not in l[2]:
            if z == "*":
                return l[2][0]*l[2][1]
            if z == "+":
                return l[2][0]+l[2][1]
        else:
            return rasp(l[2][1])

    elif type(l[1]) == tuple:
        z = l[1][0]
        if tuple() not in l[1][1]:
            if z == "*":
                return l[1][1][0] * l[1][1][1]





S = "?"
V = "!"
t = 5
V0 = 10
a = 2


print(culc((S, V, t, V0, a)))
