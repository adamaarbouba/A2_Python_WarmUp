list = []
txt_list = []
obj = {}
key = None
value = None

with open("data/exercice.txt", "r") as file:
    data = file.readlines()

for i in data:
    txt_list.append(i.strip().split(" ", 1))

for index, i in enumerate(txt_list):
    key = i[0]
    value = i[1]
    if key not in obj:
        obj[key] = [value]
    else:
        obj[key].append(value)

print(obj)

with open("data/resume_logs.txt", "w") as file:
    for i in obj.items():
        file.write(f"{i[0]} {len(i[1])} \n")
