'''write a program that has a class,student that stores roll no, name and marks in 3 subjects of the students
display the information roll no name and total marks stored about the students'''


# class Student: 
#     def __init__(self, roll_no, name, marks): 
#         self.roll_no = roll_no
#         self.name = name
#         self.marks = marks

#     def display(self): 
#         print(f"Roll No.: {self.roll_no}")
#         print(f"Name: {self.name}")
#         print(f"Total Marks: {sum(self.marks)}")

# student1 = Student(1, "Alice", [80, 70, 90])
# student2 = Student(2, "Bob", [90, 80, 70])
# student3 = Student(3, "Charlie", [70, 90, 80])

# student1.display()
# student2.display()
# student3.display()

class student:
    def __init__(self,n,r,m1,m2,m3):
        self.n=n
        self.r=r
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def display(self):
        print(self.n)
        print(self.r)
        print(self.m1 + self.m2 + self.m3)
        
Name=input("Enter your name")
Rollno=int(input("Enter your roll no"))
m1=int(input("Enter the marks in subject 5"))
m2=int(input("Enter the marks in subject 4"))
m3=int(input("Enter the marks in subject 3"))
s=student(Name,Rollno,m1,m2,m3)
s.display()

