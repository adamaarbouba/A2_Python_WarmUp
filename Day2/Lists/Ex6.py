L = [10, 20, 30, 40, 50]


def rechercheElement(elem, list):
    for index, x in enumerate(list):
        if x == elem:
            return index
    return False


# rechercheElement(30, L)
# rechercheElement(100, L)
print(rechercheElement(30, L))
print(rechercheElement(100, L))
