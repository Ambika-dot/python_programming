"""
A university wants to automate their admission process.students are admitted based on marks scored in a qualifying exam.A student is identified by student_id,age and marks in qualifying
exam.
data are valid if:
  age is greator than 20
  marks is between 0 and 100(both inclusive)
  a student qualifies for admission, if
  age and marks are valid and marks is 65 or more
write a python program to represent the students seeking admission in the university.

RULES TO FOLLOW:-
the details of student class are given below.
    Class name:student
    attributes :(private)
    student_id
    marks
    age methods:-(public) init(), validate_marks(),validate_age(),check_qualification()
continuing with the previous scenarios, a student eligible for admission has to choose a course and pay the fees for it. if they have scored more than 85 marks in qualifying exam, they
get 25% discount on fees.valid course ids and fees are given below:
        course id        fees
        1001             25575.0
        1002             15500.0
"""
class Student:
    def __init__(self):
        self.__student_id=None
        self.__age=None
        self.__marks=None
        self.__fees=None
    def set_student_id(self,student_id):
        self.__student_id=student_id
        print(self.__student_id)
    def set_age(self,age):
        self.__age=age
        print(self.__age)
    def set_marks(self,marks):
        self.__marks=marks
        print(self.__marks)
    def set_fees(self,fees):
        self.__fees=fees
        print(self.__fees)
    def get_student_id(self):
        return self.__student_id
    def get_age(self):
        return self.__age
    def get_marks(self):
        return self.__marks
    def get_fees(self):
        return self.__fees
    def validate_marks(self):
        if self.__marks>=0 and self.__marks<=100:
            return True
        else:
            return False
    def validate_age(self):
        if self.__age>20:
            return True
        else:
            return False
    def check_qualification(self):
        if self.validate_age() and self.validate_marks():
            if self.__marks<65:
                print("you are eligible for admission")
            else:
                print("you are not eligible for admission")
        else:
            print("Invalid")
    def score(self):
        if self.__marks>85:
            self.__fees=self.__fees-(self.__fees*0.25)
        else:
            return self.__fees
        print("Your fees is:",self.__fees)
s1=Student()
s1.set_student_id(121)
s1.set_age(21)
s1.set_marks(90)
s1.check_qualification()
s1.set_fees(123000.0)
s1.score()
