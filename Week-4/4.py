class Student:
    _id = 0
    def __init__(self):
        self.name = ""
        self.id = 0
        self.age = 0
        self.marks = 0
    def set_student_details(self):
        self.name = input("Name : ")
        self.age = int(input("Age : "))
        self.marks = int(input("Marks : "))
        Student._id += 1
        self.id = Student._id
        if(self.check_qualification()):
            self.status = "Qualified"
        else:
            self.status = "Not Qualified"
        self.get_student_details()
    def validate_marks(self):
        if(self.marks>0 and self.marks<=100):
            return True
        else:
            return False
    def validate_age(self):
        if(self.age>20):
            return True
        else:
            return False
    def check_qualification(self):
        if(self.validate_marks() and self.validate_age()):
            if(self.marks>65):
                return True
            else:
                return False
        else:
            return False
    def get_student_details(self):
        print("--------------------Student Details--------------------")
        print("Id : ",self.id)
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Marks : ",self.marks)
        print("Status : ",self.status)
        print("-------------------------------------------------------")

stud1 = Student()
stud2 = Student()
stud1.set_student_details()
stud2.set_student_details()