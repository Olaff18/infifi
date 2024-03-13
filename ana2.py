def silnia(n):
    if n > 1:
        return n*silnia(n-1)
    return 1

def newton(dl, zera):
    l = silnia(dl)
    m = silnia(zera)*silnia(dl-zera)
    return(l/m)
with open('pana.txt','r') as anagramy:
    ana = []
    pos = []

    for anagram in anagramy:
        j=0
        z=0
        c=0
        anagram = anagram.strip()
        if len(anagram) == 8:

            for a in anagram:
                if int(a) == 0:
                    z+=1
                else:
                    j +=1
            an = newton(len(anagram)-1,z)
            ana.append(anagram)
            pos.append(an)
m = max(pos)
t = []
for i in range(len(pos)):
    if pos[i] == m:
        t.append(ana[i])


print(t)