class Student:
    pass
    def __init__(self, N, R):
        self.name = N
        self.rollno = R
    def getData(self):
        self.name = input("Enter name - ")
        self.rollno = input("Enter Roll no - ")


class GetStudent(Student):
    def show(self):
        print("Name - ", self.name)
        print("Rollno - ", self.rollno)


s1 = GetStudent("", "")
s1.getData()
s1.show()
