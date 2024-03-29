class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def getData(self):
        self.name = input("Enter Name - ")
        self.department = input("Enter Department - ")
        self.salary = input("Enter salary - ")

    def showData(self):
        print("Name - ", self.name)
        print("Department - ", self.department)
        print("Salary - ", self.salary)


a = Employee("", "", "")
a.getData()
a.showData()

