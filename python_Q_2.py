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

"""
Q-14:the goal is to tokenize the following 5 sentences into words, excluding the stop words.
input:
sentences = ["a new world record was set","in the holy city of ayodhya","on the eve of diwali on tuesday",
"with over three lakh diya or earthen lamps","lit up simultaneously on the banks of the sarayu river"]
stopwords = ['for','was', 'a','the','and','to','in','on','with']
"""

sentences = ["a new world record was set",
             "in the holy city of ayodhya",
             "on the eve of diwali on tuesday",
             "with over three lakh diya or earthen lamps",
             "lit up simultaneously on the banks of the sarayu river"]
stopwords = ['for','was', 'a','the','and','to','in','on','with']
result=[]
for sentence in sentences:
    row_data=[]
    for word in sentence.split():
        if word not in stopwords:
            row_data.append(word)
    result.append(row_data)
print(result)

#list comprehension
print([[word for word in sentence.split() if word not in stopwords]for sentence in sentences])

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

"""
Q-17:given a number n, write a program to find the sum of the largest prime factors of
each of nine consecutive numbers starting from n.
g(n) = f(n)+f(n+1)+f(n+2)+f(n+3)+f(n+4)+f(n+5)+f(n+6)+f(n+7)+f(n+8)
where, g(n) is the sum and f(n)is the largest prime factor of n
for example,
g(10)=f(10)+f(11)+f(12)+f(13)+f(14)+f(15)+f(16)+f(17)+f(18)
     = 5 +11 +3 +13 +7 +5 +2 +17 +3
     =66
"""

def largest_prime_factor(n: int) -> int:
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

n = 10 
count = 9 

sum_of_largest_prime_factors = 0
for i in range(n, n+count):
    lpf = largest_prime_factor(i)
    sum_of_largest_prime_factors += lpf

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

"""
Q-19:Care hospital wants to know the medical speciality visited by the maximum number of patients.Assume that the patient id of the patient
along with the medical speciality visited by the patient is stored in a list.The details of the medical specialities are stored in a dictionary
as follows:
{"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
Write a function to find the medical speciality visited by the maximum number of patients and return the name of the speciality.
Note:1.Assume that there is always only one medical speciality which is visited by maximum number of patients.
2.Perform case sensitive string comparison whenever necessary.
sample input                                           expected output
[101,P,102,O,302,P,305,P]                              Pediatrics
[101,O,102,O,302,P,305,E,401,O,656,O]                  Orthopedics
[101,O,102,E,302,P,305,P,401,E,656,O,987,E]            ENT
"""
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    max_visit=0
    P=patient_medical_speciality_list.count('P')
    E=patient_medical_speciality_list.count('E')
    O=patient_medical_speciality_list.count('O')
    if P>E and P>O:
        speciality=medical_speciality['P']
    elif E>O:
        speciality=medical_speciality['O']
    else:
        speciality=medical_speciality['O']
    return speciality
patient_medical_speciality_list=[301,'P',302,'P',305,'P',401,'E',656,'E']
medical_speciality={'P':'Pediatrics','O':'Orthopedics','E':'ENT'}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)

"""
Q-20:Write a python program to display all the common characters between two strings. Return -1 if there are no matching characters.
Note: Ignore blank spaces if there are any.Perform case sensitive string comparison whenever necessary.
sample input                     expected output
"I like Python"
"Java is a very popular language"    lieyon
"""
def commom_character(str1,str2):
    str=""
    for i in str1:
        if i in str2:
            if i not in str:
                str=str+i
    if(str):
        return str.replace(" "," ")
    else:
        return -1
str1=str(input())
str2=str(input())
print(commom_character(str1,str2))
