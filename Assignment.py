#Assignment1
#Name: Jahanvi
#S.ID: 20102021
#QUESTION 1
a=int(input("First Number is "))
b=int(input("Second Number is "))
c=int(input("Third Number is "))

print("The average of numbers is : ", (a+b+c)/3)


#QUESTION 2
#All values are in $s
#standard deduction=10000
#Dependent_deduction=3000
#There is a $3000 deduction for each dependents
a=float(input("Gross income is "))
b=int(input("Number of dependents is "))
taxable_income=a-10000-(3000*b)
#tax rate=20%
tax=taxable_income*0.2
print("income tax= ", tax)


#QUESTION 3
a=int(input("Enter SID "))
b=input("Enter NAME ")
c=input("Enter GENDER(M/F/U) ")
d=input("Enter COURSE NAME ")
e=float(input("Enter CGPA "))
list=['name', 'SID', 'Gender', 'Course Name', 'CGPA']
print(list)
student=[a,b,c,d,e]
print(student)


#QUESTION 4
a=int(input("Marks of first student "))
b=int(input("Marks of second student "))
c=int(input("Marks of third student "))
d=int(input("Marks of fourth student "))
e=int(input("Marks of fifth student "))
Marks=[a,b,c,d,e]
print("list: ", Marks)
Marks.sort()
print("Sorted list: ",Marks)


#QUESTION 5(a)
color=["Red","Green","White","Black","Pink","Yellow"]
#to remove value at 4th place=> removing value at 3rd index.
color.pop(3)
print(color)

#QUESTION 5(b)
color=["Red","Green","White","Black","Pink","Yellow"]
color=["Purple"if x=="Black"or x=="Pink" else x for x in color]
print(color)


======================C:\Users\bansa>python "C:\Users\bansa\Desktop\assign\q3.py"==============================================================
First Number is 52
Second Number is 45
Third Number is 63
The average of numbers is :  53.333333333333336
>>>

======================C:\Users\bansa>python "C:\Users\bansa\Desktop\assign\q3.py"==============================================================
Gross income is 50000
Number of dependents is 4
income tax=  5600.0
>>>

======================C:\Users\bansa>python "C:\Users\bansa\Desktop\assign\q3.py"===============================================================
Enter SID 20102021
Enter NAME Jahanvi
Enter GENDER(M/F/U) F
Enter COURSE NAME Intro to computing
Enter CGPA 7.3
['name', 'SID', 'Gender', 'Course Name', 'CGPA']
[20102021, 'Jahanvi', 'F', 'Intro to computing', 7.3]
>>>

======================C:\Users\bansa>python "C:\Users\bansa\Desktop\assign\q3.py"===============================================================
Marks of first student 68
Marks of second student 49
Marks of third student 75
Marks of fourth student 95
Marks of fifth student 82
list:  [68, 49, 75, 95, 82]
Sorted list:  [49, 68, 75, 82, 95]
>>>

======================C:\Users\bansa>python "C:\Users\bansa\Desktop\assign\q3.py"===============================================================
['Red', 'Green', 'White', 'Pink', 'Yellow']
>>>

======================C:\Users\bansa>python "C:\Users\bansa\Desktop\assign\q3.py"===============================================================
['Red', 'Green', 'White', 'Purple', 'Purple', 'Yellow']
>>>






