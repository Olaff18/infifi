with open('anagramy.txt', 'r') as anagramy:
    zero = 0
    x = 0
    max = 0
    l = 0
    for anagram in anagramy:
        x = 0
        tab = []
        suma = 0
        anagram = anagram.strip()
        dz = int(anagram,2)
        for i in str(dz):
            if i not in tab:
                tab.append(i)
            if i == '0':
                x = 1
        if x == 0:
            zero += 1
        for i in tab:
            suma += int(i)
        if suma>max:
            max = suma
            l = dz

print(zero,l)

#728 7896


