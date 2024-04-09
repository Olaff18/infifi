with open('liczby.txt', 'r') as plik:
    liczba = 0
    roznica = 0
    for l in plik:
        l = l.strip()
        r = l[::-1]
        ab = abs(int(r)-int(l))
        if ab > roznica:
            liczba = int(l)
            roznica = ab

print(liczba, roznica)
#1129 8082