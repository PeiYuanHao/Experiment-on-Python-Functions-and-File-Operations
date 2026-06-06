with open('test.txt', 'r', encoding='utf-8') as f:
    t = f.read()

temp = t.upper()

with open('test_copy.txt', 'w', encoding='utf-8') as f:
    f.write(temp)