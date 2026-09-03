text = "I Was  HUGGGGGE fan of Freed Again i will visit his concert once"

splited_text = text.split()


print(splited_text)

# for index, i in enumerate(splited_text):
#     if len(i) <= 3:
#         splited_text.remove(i)
#     else:
#         splited_text[index] = i.lower()

splited_text = [word.lower() for word in splited_text if len(word) > 3]


print(splited_text)
