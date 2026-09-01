print("Hello In The Programe")

name = input("May you enter your name pls: \n")
wage = input("May you enter your wage pls: \n")
hours = input("May you enter your hour pls: \n")

hours = int(hours)
wage = float(wage)

if (hours < 40):
    Twage = hours * wage
else:
    Twage = hours * (wage * 1.5)

Twage = str(Twage)

print(name + "Your Total wage is : " + Twage)
