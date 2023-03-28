"""
Q-7:Write a python function which accepts a string and returns a string made of the first 2 and the last 2 characters of the given string.If the string length is less than 2,return -1.
Note:If the string length is equal to 2, consider the 2 characters to be the first as well as the last two characters.

Sample input                           Expected output
w3resource                                  w3ce
w3                                          w3w3
A                                           -1

"""
def function1(str1):
    if len(str1)<2:
        return -1
    else:
        return str1[0:2]+str1[-2:]
print(function1("w3resource"))
print(function1("w3"))
print(function1("A"))

