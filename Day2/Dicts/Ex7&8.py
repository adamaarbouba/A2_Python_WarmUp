# etudiants = [
#     {"nom": "Omar",
#      "age": 22,
#      "note": 15},
#     {"nom": "Sara", "age": 21, "note": 17},
#     {"nom": "Yassine", "age": 23, "note": 9},
#     {"nom": "Imane", "age": 20, "note": 13},
#     {"nom": "Hamza", "age": 24, "note": 7}
# ]

# admi = []
# not_admi = []

# for ele in etudiants:
#     for key, value in ele.items():
#         if key == "note" and value >= 10:
#             admi.append(ele)
#         elif key == "note" and value < 10:
#             not_admi.append(ele)

# print(admi)
# print(not_admi)


# def avg(list):
#     x = []
#     j = 0
#     for ele in etudiants:
#         for key, value in ele.items():
#             if key == "note":
#                 x.append(value)
#         j = sum(x) // len(x)
#     return j


# print(avg(etudiants))

# x = []
# j = 0
# top_student = []

# for ele in etudiants:
#     for key, value in ele.items():
#         if key == "note":
#             x.append(value)

# for ele in etudiants:
#     for key, value in ele.items():
#         if key == "note" and max(x) == value:
#             top_student = ele

# print(top_student)

# top_student = max(etudiants, key=lambda x: x["note"])

# print(top_student)


'''>>> 8'''

# ventes = [
#     {"produit": "PC",
#      "categorie": "Informatique", "prix": 8000, "quantite": 2},
#     {"produit": "Souris",
#      "categorie": "Accessoire", "prix": 150, "quantite": 10},
#     {"produit": "Clavier",
#      "categorie": "Accessoire", "prix": 300, "quantite": 5},
#     {"produit": "PC",
#      "categorie": "Informatique", "prix": 8000, "quantite": 1},
#     {"produit": "Écran",
#      "categorie": "Informatique", "prix": 2500, "quantite": 3}
# ]

# ventes_total = len(ventes)

# print(ventes_total)


# CA = 0
# for ele in ventes:
#     CA += ele["quantite"] * ele["prix"]

# print(CA)


# x = []
# j = 0
# top_product = {}
# q = 0

# for ele in ventes:
#     for key, value in ele.items():
#         if key == "prix":
#             x.append(value)

# for ele in ventes:
#     for key, value in ele.items():
#         if key == "prix" and max(x) == value:
#             q += ele["quantite"]
#             top_product["quantite"] = q
#             top_product["produit"] = ele["produit"]

# print(top_product)
