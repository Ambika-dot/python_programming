"""

Q-1:Write a python to find and display product of three positive integer values based on the rule mentioned below.It should display the product of the three values except when one of the
integer value is 7. In that case, 7 should not be include in the product and the values to its left also should not be included.If there is only one value to be considered,display that
value itself.If no values can be included in the product,display -1.
Note:Assume that if 7 is one of the positive integer values,then it will occur only once.Refer the sample I/O
given below.
Sample input     expected output
1,5,3                 15
3,7,8                  8
7,4,3                 12
1,5,7                 -1


"""

num1=int(input())
num2=int(input())
num3=int(input())
if num1==7:
    print(num2*num3)
elif num2==7:
    print(num3)
elif num3==7:
    print(-1)
else:
    print(num1*num2*num3)
