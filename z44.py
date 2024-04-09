with open('liczby.txt','r') as plik:
    a = plik.readlines()
    
    for l in range(len(a)):
        a[l] = a[l].strip()
    uni = len(set(a))
    d = 0
    t = 0
    # for i in range(10,10000):
    #     if a.count(str(i)) == 2:
    #         d+=1
    #     if a.count(str(i)) == 3:
    #         t+=1
    # print(d,t)    
    z = set(a)
    for i in z:
        if a.count(i) == 2:
            d+=1
        elif a.count(i) == 3:
            t+=1
    print(uni,d,t)
    #85 13 1