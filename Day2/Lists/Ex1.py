fruite = ["Apple", "Banana", "Orange", "Kiwi", "Mangue", "Strawberry"]

'''
>>> A

for x in fruite:
    print("Fruit: ", x)

print("The First Fruit in The Basket is: ", fruite[0])

print("The Last Fruit in The Basket is: ", fruite[-1])

print("The Theird Fruit in The Basket is: ", fruite[2])

'''


'''

>>> B

i = 0

for x in fruite:
    if i <= 2:
        print(x)
        i += 1
    else:
        break

j = len(fruite) - 1

for x in fruite:
    if i <= 2:
        print(fruite[j])
        i += 1
        j -= 1
    else:
        break

print(fruite[::2])
'''


'''

>>> C

fruite = [s.replace('Orange', 'Aananas') for s in fruite]

fruite[fruite.index("Orange")] = "Ananas"


print(fruite[::1])

'''
