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

