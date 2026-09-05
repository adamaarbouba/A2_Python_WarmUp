# def factorial(n):
#     if (n == 0 or n == 1):
#         return 1
#     result = 1

#     for i in range(1, n + 1):
#         result *= i

#     return result


# print(factorial(5))


# def Multi10(m, multi):
#     list = []
#     if (m == 0 or multi == 0):
#         return list.append(0)
#     for i in range(1, multi + 1):
#         list.append(m * i)
#     return list


# print(Multi10(1, 10))


# def perfect_square(L):
#     if L < 0:
#         return False
#     if L == 0:
#         return True

#     for i in range(1, L + 1):
#         if i * i == L:
#             return True
#         if i * i > L:
#             return False


# print(perfect_square(20))
# print(perfect_square(25))


# def str_split(str):
#     if len(str) == 0:
#         return False
#     for i in str:
#         print(i)


# str_split("Hello World")

# def long_str(text):
#     max_str = ""

#     if len(text) == 0:
#         return False

#     splited_txt = text.split(" ")

#     for i in splited_txt:
#         if len(i) > len(max_str):
#             max_str = i

#     return max_str


# ch = "Hello World You Are not going to make it alive if you bombastic"
# print(long_str(ch))


# def compterOccurrences(elem, text):
#     count = 0

#     for i in text:
#         if i.lower() == elem.lower():
#             count += 1

#     return count


# def frequency(text):
#     tab = {}

#     for x in text:
#         key = x.lower()

#         if key not in tab:
#             tab[key] = compterOccurrences(x, text)

#     return tab


# def char_occurrences(text):
#     return frequency(text)


# ch = "Hello HELLO"
# print(char_occurrences(ch))
