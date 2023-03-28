"""
Q-16:string rotation
input:  rhdt:246,ghftd:1246
exp1: here every string is associated with the number sep by:
--> if sum of squares of digits is even then rotate the string by 1
--> if sum of squares of digits is odd then rotate the string left by 2 position
2*2+4*4+6*6=56 which is even so rhdt = trhd
1*1+2*2+4*4+6*6=57 which is odd so rotate left by 2 so ghftd=ftdgh
"""

s=input().split(",")
stt=[]
numm=[]
for i in s:
    s1,n=i.split(":")
    stt.append(s1)#stt=[rhdt,ghftd]
    numm.append(n)#numm=[246,1246]
def rotate (ss,n):
    n=str👎
    s=0
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1] #rhdt   t+rhd
    else:
        return ss[2:]+ss[:2] # ghftd   ftdgh
for i in range(len(numm)): #i=0
    print(rotate(stt[i],numm[i]))

