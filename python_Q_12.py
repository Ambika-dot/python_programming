"""
Q-12:find the number of distinct subarrays in an array of position integers such that the sum of the subarray is an odd integer, two subarray are considered different if they start or end at
different index input.

1
3
1 2 3
[1]  [1 2]  [1,2,3]  [2]  [2,3]  [3]
4
"""

n1=int(input())
n2=int(input())
array=[i for i in range(n1,n2+1)]
print(array)#[1,2,3]
result=[]
for i in range(len(array)):#i=1
    for j in range(i,len(array)):#j=1,2
        result.append(array[i:j+1])#[0:1]=[1],
print(result)                       #[0:2]=[1,2]
