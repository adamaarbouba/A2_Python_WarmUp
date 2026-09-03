print("Hello In The Programe")

Nnum = int(input("May you enter your Nnum pls: \n"))

while (Nnum != 1):
    if (Nnum % 2 == 0):
        Nnum = Nnum // 2
    elif (Nnum % 2 == 1):
        Nnum = (3 * Nnum) + 1
    print(Nnum)
