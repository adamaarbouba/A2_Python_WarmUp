notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]

# print(notes)


def avg(list):
    x = sum(list) // len(list)
    return x


# print(avg(notes))

# aboveAvg = []

# for x in notes:
#     if avg(notes) < x:
#         aboveAvg.append(x)

# print(aboveAvg)

# underAvg = []

# for x in notes:
#     if avg(notes) > x:
#         underAvg.append(x)

# print(underAvg)

# print("The Highest Note is:", max(notes),
#       "\nThe Lowset Note is:", min(notes))

# j = 0

# for i in notes:
#     if i >= 10:
#         j += 1

# mR = int((j / len(notes)) * 100)

# print(mR)
