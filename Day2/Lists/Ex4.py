temp = [18, 25, 31, 14, 27, 35, 22, 19, 30, 12, 28]

lowTemp = []
highTemp = []
Mtemp = []
count = 0

for i in temp:
    if i < 25:
        lowTemp.append(i)

for i in temp:
    if i >= 25:
        highTemp.append(i)

for i in temp:
    if i in range(20, 30):
        Mtemp.append(i)

for i in temp:
    if i > 30:
        count += 1

print("Low temps are: ", lowTemp)

print("High temps are: ", highTemp)

print("Mteps are: ", Mtemp)

print("The number of temps higher then 30 is: ", count)
