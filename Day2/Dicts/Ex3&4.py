notes = {"Python": 15, "SQL": 13, "JavaScript": 17, "Git": 14, "Linux": 12}
notes_etudiants = {
    "Omar": 15,
    "Sara": 8,
    "Yassine": 17,
    "Imane": 11,
    "Hamza": 6,
    "Nadia": 14
    }

# for x in notes:
#     print(x)

# for x in notes:
#     print(x.keys())

# for key, value in notes.items():
#     print(f"Key : {key}, value : {value}")
# print(list(notes.items()))


# def avg(dict):
#     x = []
#     j = 0
#     for i in dict.values():
#         x.append(i)
#     j = sum(x) // len(x)
#     return j


# print(max(notes.values()))
# print(min(notes.values()))
# print(avg((notes)))

# low_score = {}
# high_score = {}
# for key, value in notes_etudiants.items():

#     if value >= 10:
#         high_score[key] = value
#     else:
#         low_score[key] = value

# print(f"The high Score is {high_score} \nThe lower Score is {low_score}")
