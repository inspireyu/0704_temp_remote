# 质数(分解质因数)
print("分解质因数\n\n请你给出一个数，让我来对它进行分解质因数的操作。", end="")
a = int(input("你要给出的数是："))
print(f"\n{a}=", end="")
b = int(a)
y = int(0)
for i in range(2, a):
    x = int(0)
    for j in range(2, b):
        if b % j == 0:
            x = x + 1
            y = y + 1
            if y == 1:
                print(j, end="")
                b = b // j
                break
            elif y != 1:
                print(f"*{j}", end="")
                b = b // j
                break
    if x == 0 and y != 0:
        print(f"*{b}")
        break
    elif x == 0 and y == 0:
        print(b)
        break

