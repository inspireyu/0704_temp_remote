import random
num = random.randint(1,101)

for i in range(1,11):
    ipt = int(input("Your number is:"))
    if ipt > num:
        print("Too big", end = "")
    elif ipt < num:
        print("Too small", end = "")
    elif ipt == num:
        print(f"Yes, It's {num}. Exit.")
        break
    if i < 10:
        print(", try again.")
    elif i == 10:
        print(".\nYou lost.")