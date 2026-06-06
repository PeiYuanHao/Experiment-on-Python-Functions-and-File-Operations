def cnt(name):
    with open(name, 'r', encoding = 'utf-8') as f:
        t = f.read()

    a = sum(1 for c in t if 'A' <= c <= 'Z')
    b = sum(1 for c in t if 'a' <= c <= 'z')
    c = sum(1 for c in t if '0' <= c <= '9')

    print(f"大写字母的频率为:{a}, 百分比为:{a / (a + b + c) * 100 : .2f} %")
    print(f"小写字母的频率为:{b}, 百分比为:{b / (a + b + c) * 100 : .2f} %")
    print(f"数字的频率为:{c}, 百分比为:{c / (a + b + c) * 100 : .2f} %")

cnt('test.tnt')

def cnt2(name):
    d = {'大写字母': 0, '小写字母': 0, '数字': 0}

    with open(name, 'r', encoding = 'utf-8') as f:
        t = f.read()

    for ch in t:
        if 'A' <= ch <= 'Z':
            d['大写字母'] += 1
        elif 'a' <= ch <= 'z':
            d['小写字母'] += 1
        elif '0' <= ch <= '9':
            d['数字'] += 1

    total = sum(d.values())
    for key, value in d.items():
        print(f"{key}的频率为:{value}, 百分比为:{value / total * 100 : .2f} %")

cnt2('test.txt')

