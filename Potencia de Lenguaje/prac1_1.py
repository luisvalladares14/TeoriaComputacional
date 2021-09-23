def pot(n1, n2):
    print(n2*n1)

def potencia(n1):
    #print(n1)
    alf = n1
    alf_new = []
    for i in n1:
        for j in alf:
            alf_new.append(i+j)
    n1 = alf_new
    return n1

def pot_mas(n1, n2, n3):
    alfa_new = []
    x=2
    if x<n3:

        for i in n1:
            for j in n2:
                alfa_new.append(i+j)
        pot_mas(alfa_new,n2, n3-1)
    print(alfa_new)
