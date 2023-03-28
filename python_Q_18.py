"""
Q-18:Write a python function, nearest_palindrome() which accepts a number and returns the nearest palindrome greater than the given number.
sample input                    expected output
99                                 101
1221                                1331
"""
def nearest_palindrome(num):
    num+=1
    while str(num)!= str(num)[::-1]:
        num +=1
    return num
num=int(input())
print(nearest_palindrome(num))
