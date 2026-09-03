L = [7, 23, 5, 23, 7, 19, 23, 12, 29, 7, 5]


def compterOccurrences(elem, list):
    count = 0
    for i in list:
        if i == elem:
            count += 1
    return count


def frequency(list):
    tab = {}

    for index, x in enumerate(list):
        if [x, compterOccurrences(x, list)] not in tab.values():
            tab[index] = [x, compterOccurrences(x, list)]
    return tab


# print(frequency(L))
