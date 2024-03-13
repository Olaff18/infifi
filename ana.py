with open('anagramy.txt', 'r') as anagramy:
    c = 0
    p = 0
    for anagram in anagramy:
        j = 0
        z = 0
        anagram = anagram.strip()
        for a in anagram:
            a = int(a)
            if a == 0:
                z+=1
            else:
                j+=1

        if j == z:
            c+=1
        elif j-1==z or j+1==z:
            p+=1
print(c, p)
#118 219