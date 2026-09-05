txt_list = []
obj = {}
key = None
value = None

with open("data/exercice.txt", "r") as file:
    data = file.readlines()

    for i in data:
        txt_list.append(i.split(" ", 1))

for index, i in enumerate(txt_list):
    key = i[0]
    value = i[1]
    obj[index] = {key: value}

# print(obj)

with open("data/obj.txt", "w") as file:
    for i in obj.values():
        for key, value in i.items():
            file.write(f"{key} {value}")

# with open("data/obj.txt", "w") as file:
#     for i in obj.values():
#         for key, value in i.items():
#             file.write(f"{i}\n")
