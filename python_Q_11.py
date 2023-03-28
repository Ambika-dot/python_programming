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


