import Ex8 as feq


info = ["Omar", 25, "Casablanca", 15.5, True]


def typeCount(List):
    list = []

    for i in List:
        list.append(type(i).__name__)

    return feq.frequency(list)


types = typeCount(info)

# print(types)


def typeNum(List):
    list = []
    numbers = ["int", "float"]

    for i in info:
        if type(i).__name__ in numbers:
            list.append(i)

    return list


listNum = typeNum(info)

# print(listNum)
