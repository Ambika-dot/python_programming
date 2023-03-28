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
