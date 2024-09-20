def Palcheck(str):
    reversestr = str[::-1]
    if str == reversestr:
        return True
    else:
        return False
str = str(input("Enter your String: "))
print(Palcheck(str))