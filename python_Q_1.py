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
"""
Q-2:A traveler on a visit to India is in need of some Indian Rupees(INR) but he has money belonging to another currency.He wants to know how much money he should provide in the currency he
has,to get the specified amount in INR.Write a python program to implement a currency calculator which accepts the amount needed in INR and the name of the currency which the traveler
has.The program should identify and display the amount the traveler should provide in the currency he has, to get the specified amount in INR.
Note: Use the forex information provided in the table below for the calculation.Consider that only the currency names mentioned in the table are valid.For any invalid currency name,
display -1.
Currency                       Equivalent of 1.00 INR
Euro                                  0.01417
British Pound                         0.0100
Austrian Dollar                       0.02140
Canadian Dollar                       0.02027

"""

def currencycal(AmountINR,curr):
    if curr=="Euro":
        print(AmountINR*0.01417)
    elif curr=="British Pound":
        print(AmountINR*0.0100)
    elif  curr=="Austrian Dollar":
        print(AmountINR*0.02140)
    elif curr=="Canadian Dollar":
        print(AmountINR*0.02027)
    else:
        print(-1)
currencycal(300,"Euro")
currencycal(300,"British Pound")
currencycal(300,"Austrian Dollar")
currencycal(300,"Canadian Dollar")

"""
Q-3:The flight ticket rates for a round-trip(Mumbai->Dubai) were as follows: Rate per Adult: Rs. 37550.0 , Rate per Child: 1/3rd of the rate per adultService Tax: 7% of the ticket amount
(including all passengers). As it was a holiday season, the airline also offered 10% discount on the final ticket cost(after inclusion of the service tax). Find and display the total
ticket cost for a group which had adults and children.

Sample Input         expected output
Number of adults      Number of children
5                      2    Total ticket cost:204910.35
3                      1    Total ticket cost:120535.5

"""

n_adults=int(input("Enter the number of adults: "))
n_childs=int(input("Enter the number of childs: "))
total=((((n_adults*37550.0)+(n_childs*37550.0/3))*1.07)*0.90)
"""print(total)
total1=total*0.07
total2=total+total1
print("with ur service tax",total2)
total_amount=total2*0.90
print(total_amount)
"""

"""
Q-4:You have x no. of 5 rupee coins and y no. of 1 rupee coins.You want to purchase an item for amount z. The shopkeeper wants you to provide exact change. You want to pay using minimum number
of coins will you use ?
If exact change is not possible then display -1.
Sample input                                                              Expected output
available Rs. 1 coins  available Rs. 5 notes   amount to be made      Rs. 1 coins needed     Rs. 5 notes needed
       2                          4                        21                  1               4
      11                          2                        11                  1               2
       3                          3                        19                 -1

"""
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0

    five = int(rupees_to_make/5)
    one_needed = rupees_to_make%5
    five_needed = five if five <= no_of_five else no_of_five
    if (five > no_of_five):
        one_needed = rupees_to_make - 5 * no_of_five     
    
    (print("No. of Five needed : {}\nNo. of One needed  : {}".format(five_needed,one_needed))) if one_needed <= no_of_one else (print(-1))

make_amount(int(input()),int(input()),int(input()))

"""
Q-5:Write a python function which accepts a sentence and finds the number of letters and digits in the sentence. It should return a list in which the first value should be letter count and
second value should be digit count.Ignore the spaces or any other special character in the sentence.

Sample input       Expected output

Infosys 123         [7,3]
ABCEFG              [6,0]
"""

def function(str1):
    l_count=0
    d_count=0
    for i in str1:
        if i.isalpha():
            l_count=l_count+1
        elif i.isdigit():
            d_count=d_count+1
        else:
            continue
    return [l_count,d_count]
print(function("Infosys 123"))
print(function("ABCEFG"))

"""
Q-6:Write a python function, find_pairs_of_numbers() which accepts a list of positive integers with no repetitions and returns count of pairs of numbers in the list that adds up to n.The
function should return 0,if no such pairs are found in the list.

Sample input                                         Expected output
[1,2,7,4,5,6,0,3],6                                       3  (1,5)(2,4)(6,0)
[3,4,1,8,5,9,0,6],9                                       4  (3,6)(4,5)(1,8)(9,0)

"""
def find_pairs_of_numbers(num_list,n):
    count=0
    for x in num_list:  #[1,2,7,4,5,6,0,3]
        index=num_list.index(x)+1 #index=1
        for y in range(index,len(num_list)): #1,7
            if x+num_list[y]==n:  #1+2==6
                count+=1  #count=0
    return count
num_list=[1,2,7,4,5,6,0,3]
n=6
print(find_pairs_of_numbers(num_list,n))

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

"""
Q-8:Write a python function to add 'ing' at the end of a given string and return the new string.If the given string already ends with 'ing' then add 'ly'.If the length of the given string is
less than 3, leave it unchanged.

Sample input                  Expected output
sleep                             sleeping
amazing                         amazingly
is                                 is

"""
def add_string(str1):  #str1=string
    length = len(str1)  #6
    if length>2:
        if str1[-3:]=="ing":
            str1+="ly"
        else:
            str1+="ing"
    return str1
print(add_string("sleep"))
print(add_string("is"))
print(add_string("string"))

"""
Q-9:Write a python function, check_double(number) which accepts a whole number and returns True if it satisfies the given conditions.
1. The number and its double should have exactly the same number of digits.
2. Both the numbers should have the same digits , but in different order.
Otherwise it should return False.
Example: If the number is 125874 and its double, 251748, contain exactly the same digits , but in a different order.

"""
def check_double(number):
    num1=str(number*2)#490
    number=str(number)
    count=0
    for x in number:#245
        if x in num1:#490
            count+=1
        else:
            return False
    if count==len(number):
        return True
print(check_double(245))
print(check_double(125874))

"""
Q-10:A teacher is in the process of generating few reports based on the marks scored by the students of her class in a project assessment.Assume that the marks of her 10 students are available
in a tuple. The marks are out of 25.
Write a python program to implement the following functions:
1.find_more_than_average(): Find and return the percentage of students who have scored more than the average mark of the class.
2.generate_frequency(): Find how many students have scored the same marks. for example,how many have scored 0,how many have scored 1, how many have scored 3... .how many have scored 25.The
result should be populated in a list and returned.
3.sort_marks(): Sort the marks in the increasing order from 0 to 25.The sorted values should be populated in a list and returned.

sample input                                     expected output
list_of_marks = (12,18,25,24,2,5,18,20,20,21)      70.0
[0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,2,0,2,1,0,0,1,1]   [2,5,12,18,18,20,20,21,24,25]

"""
marks=(12,18,25,24,2,5,18,20,20,21)
def find_more_than_average():
    avg= sum(marks)/len(marks)
    count =0
    for mark in marks:
        if mark > avg:
            count=count+1
    return (count/len(marks))*100
def sort_marks():
    return sorted(marks)
def generate_frequency():
    freq=[]
    for mark in range(0,26):
        count=0
        for y in marks:
            if mark==y:
                count+=1
        freq.append(count)
    return freq
print(find_more_than_average())
print(generate_frequency())
print(sort_marks())

"""
Q-11:Represent a small bilingual (english-swedish) glossary given below as a python dictionary{"merry":"god,","chirstmas":"jul,","and":"och","happy":"gott","new":"nytt","year":"ar"}and use it
to translate your chirstmas wishes from english into swedish.that is, write a python function translate() that accepts the bilingual dictionary and a list of english words (your christmas
wish) and returns a list of equivalent swedish words.
"""

def translate(dict1,list1):
    list2=[]
    for i in list1:
        list2.append(dict1[i])
    return list2
dict1={"merry":"god,","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
list1=["merry","christmas"]
print(translate(dict1,list1))


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
