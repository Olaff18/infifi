with open('liczby.txt', 'r') as plik:
    rev = []

    for l in plik:
        l = l.strip()
        r = l[::-1]
        if int(r)%17==0:
            rev.append(r)

for e in rev:
    print(e)

# 1156
# 102
# 51
# 765
# 119
# 119
# 731