def makestring(spacecnt, starcnt):
    halfspace = int(spacecnt/2)
    print(halfspace)
    s =[]
    str1=""
    for i in range(halfspace):
        s.append(" ")
    for i in range(starcnt):
        s.append("*")
    for i in range(halfspace):
        s.append(" ")
    return str1.join(s)
def tower_builder(n_floors):
    totalcnt=n_floors*2-1;
    tower=[]
    for i in range(n_floors):
        spacecnt = (n_floors-1-i)*2
        starcnt = totalcnt - spacecnt
        print(spacecnt)
        tower.append(makestring(spacecnt, starcnt))
