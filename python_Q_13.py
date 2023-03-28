"""
Q-13:for each number in list_b, get the number and its position(index) in mylist as are turn list of tuples.
sample input
mylist = [9,3,6,1,5,0,8,2,4,7]
list-b = [6,4,6,1,2,2]
sample output
result = [(6,2),(4,8),...]
"""

mylist = [9,3,6,1,5,0,8,2,4,7]
list_b = [6,4,6,1,2,2]
#mylist = list(input())
#list_b = list(input())
result=[]
for element in list_b:
    result.append((element,mylist.index(element)))
print(result)
print([(element,mylist.index(element))for element in list_b])

