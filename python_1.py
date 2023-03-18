#python programming

#datatypes
name="ambika" #explicitly declared at run time
print("name",name,type(name))
#full pledge object oriented
rollno=67
print("rollno",rollno,type(rollno))
percentage=88.9
print("percentage",percentage,type(percentage))
student_y_no=True
complex_number=3+6j
print("complex_number",complex_number,type(complex_number))


#decision making statements

#read a number -->multiple 3-->multiple 5-->multiple 3 and 5 else print invalid
number=int(input("Enter an integer number"))
print(number,type(number))  #15
if number%3==0 and number%5==0:
    print("its a multiple of both")
elif number%5==0:
    print("its a multiple of 5")
elif number%3==0:
    print("its a multiple of 3")
else:
    print("invalid")
    
