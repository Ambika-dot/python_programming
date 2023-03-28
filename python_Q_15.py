"""
Q-15:input: a string of comma separated numbers. the number 5 and 8 are present in the list.
assume that 8 always comes after 5.
case1: num1 = add all the numbers which do not lie between 5 and 8 in the input
case2: num2 = number formed by concatenating all numbers from 5 to 8
output sum of num1 and num2
example
1)3,2,6,5,1,4,8,9

num1 = 3+2+6+9=20
num2 = 5148
o/p = 5148+20=5168
"""
array=list(map(int,input().split(",")))
number1=sum(array[:array.index(5)])+sum(array[array.index(8)+1:])
l=array[array.index(5):array.index(8)+1]
number2=""
for i in l:
    number2+=str(i)
print(int(number2)+number1)

