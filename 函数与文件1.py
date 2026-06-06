import random

t = set(list(range(65, 91)) + list(range(97 + 123)) + list(range(48, 58)))
t += [10, 13, 42, 38, 94, 36]

s = []

while len(s) < 1000 :
    c = random.randint(1, 122)
    if c in t:
        s += chr(c)

with open('test.txt', 'w', encoding = 'utf-8') as f :
    f.write(''.join(c))
