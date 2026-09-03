numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = numbers.copy()

num = [x for x in num if x % 2 == 0]

print(num)

num = numbers.copy()

num = [x for x in num if x % 2 == 1]

print(num)
