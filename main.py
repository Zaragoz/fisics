def culc(x, y, z, find):

    var = [x, y, z]
    formuls = [[x, "+", (("-", (("*", (8, 2, y, z)), z)), z)]]#x = (8*2*y*z) - z + z

    if var[find] == formuls[0][0]:
        while True:
            if formuls[0][0] != -1:
                break
            formuls[0][0] = rasp(formuls[0][1],formuls[0][2])
        return formuls[0][0]

    else:
        left = formuls[0][0]
        c = 1
        for i in range(len(formuls[0])):
            if formuls[0][i] == int() or formuls[0][i] == float():
                if formuls[0][i] == var[find]:
                    c += 1
            for j in range(len(formuls[0][i])):
                if formuls[0][i][j] == var[find]:
                    c+=1

        if c == 1:




def rasp(z, l):
    znach = 0
    if z == "+":
        for i in range(len(l)):
            znach += l[i]
    elif z == "-":
        znatch = l[0] - l[1]
    elif z == "*":
        znach = 1
        for i in range(len(l)):
            znach *= l[i]
    elif z == "/":
        znach = l[0]
        for i in range(1, len(l)):
            znach /= l[i]
    return znach



x = -1
y = 8
z = 9

print(culc(x,y,z))
