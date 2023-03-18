#break
for i in range(1,101):
    """if i==50:
        break"""
    print(i,end=" ")
else:
    print("else statement")
#continue

for i in range(1,101):
    if i==50:
        continue
    print(i,end=" ")
for i in range(1,101):
    if i==50:
        pass
    print(i,end=" ")
#-------------------------------------------------------------------------------------------  
#functions
def function1():
    print("its a function")
function1()
def function2(num1,num2):
    print("num1=",num1,"num2=",num2)
    #print()__str__
function2(10,20)
def function3(num1,num2):
    num3=num1+num2
    return num3
print("value returned",function3(100,200))
def function4(num1,num2):
    num3=num1+num2
    return num3
print("value returned",function4(10,20.2))
def function5(num1,num2):
    num3=num1+str(num2)
    return num3
print("value returned",function5('10',20.2))


#--------------------------------------------------------------------------------------

#categories of functions
#based on arguments
#1:positional arguments

def function1(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function1(10,20,30,40)
function1(100,"200",300,400)
function1(1,2,3,4)

#2:keyword arguments

def function2(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function2(num4=10,num1=20,num2=30,num3=40)
function2(num4=10,num1=10,num2=30,num3=40)

#3:default arguments

def function3(name,rollno,branch,collegename="GIET"):
    print(name,rollno,branch,collegename)
function3("ambika",11,"ECE")
function3("lisha",12,"CSE")
function3("chintu",13,"AGE")
function3("soumya",14,"BT")

#4:variable no of arguments

def function4(*var):#tuple=
    for i in var:
        print(i,end=' ')
function4(10,20)
print()
function4(10,20,30,40)
print()
function4(10,20,30,40,50,60)


def add(*var):#tuple=
    sum1=0
    for i in var:#10,20
        sum1=sum1+i
    return(sum1)
print(add(10,20))
print(add(10,20,30,40))
print(add(10,20,30,40,50,60))


































