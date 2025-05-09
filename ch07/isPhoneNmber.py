# Using a function named isPhoneNumber() to check whether a string matches pattern, returning either True or False.

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print("Is 312-445-3232 a phone number?")
print(isPhoneNumber("312-445-3232"))
print("Is Yoshi yoshi a phone number?")
print(isPhoneNumber("Yoshi yoshi"))
