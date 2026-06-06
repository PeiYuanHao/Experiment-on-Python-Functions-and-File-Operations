def check(n):
    res = 0
    m = n
    k = len(str(n))

    while m != 0:
        res += (m % 10) ** k
        m //= 10

    if res == n :
        return True
    
    return False

max = int(input("请输入参数 max(max >= 1000) :"))

res = []
for i in range(100, max + 1):
    if check(i):
        res.append(str(i))

print(' '.join(res))