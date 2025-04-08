# try:
#     prit(1+3)
# except IndexError as e:
#     print("Chyba")
#     print(e)
# finally:
#     print("Toto sa vykona vzdy")
#     print("aj ked nastala chyba")

# try:
#     pole = [0,1,2]
#     print(pole[100])
# except IndexError as e:
#     print("Index error")
#     print(e)

# try:
#     print(1+"a")
# except Exception as e:
#     print("Chyba")
#     print(e)
# except TypeError as e:
#     print("Chyba")
#     print(e)

# print("pokračujem")

# print(1+"a")

# print("sem sa uz nedostanem")

try:
    if 1 > 3:
        raise Exception("Chyba")
    else:
        print("Pokračujem")
except Exception as e:
    print("Chyba")
    print(e)

