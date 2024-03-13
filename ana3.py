with open('anagramy.txt', 'r') as anagramy:
    max = 0
    c = 0
    for anagram in anagramy:
        anagram = anagram.strip()
        if c == 0:
            c = 5
            a = anagram
            continue
        else:
            s = abs(int(a,2)-int(anagram,2))
            if s > max:
                max = s
            a = anagram

print(bin(max))
# 10011000111001