ipt = int(input("Your number is:"))
rem_num = ipt
otpt = f"{ipt} = 1"

is_pri = 0
pri_num = 2

if ipt == 1 or ipt == 2:
    is_pri = 1

while 1:
    for i in range(pri_num, int(rem_num)+1):
        if rem_num % i == 0:
            pri_num = i
            rem_num = rem_num / i
            break

    if rem_num == 1:
        if pri_num == ipt:
            is_pri = 1
        else:
            otpt = otpt + f" * {str(pri_num)}"
        break
    otpt = otpt + f" * {str(pri_num)}"

if is_pri == 0:
    print(otpt)
elif is_pri == 1:
    print("Prime number.")