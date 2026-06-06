import random


def play(change):
	prize = random.randint(0, 2)
	choice = random.randint(0, 2)

	door = [0, 1, 2]
	for d in door:
		if d != prize and d != choice:
			open = d
			break

	if change:
		for d in door:
			if d != choice and d != open:
				choice = d
				break

	return choice == prize


n = 10000
win = 0
lose = 0

for i in range(n):
	if play(True):
		win += 1
	if play(False):
		lose += 1

print(f"模拟次数:{n}")
print(f"改变选择获胜次数:{win}, 获胜概率:{win / n * 100:.2f}%")
print(f"不改变选择获胜次数:{lose}, 获胜概率:{lose / n * 100:.2f}%")

if win > lose:
	print("应该改变一开始的选择")
else:
	print("不应该改变一开始的选择")
