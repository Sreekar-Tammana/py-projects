# Creating the class named Programmer and fill the Details

class Programmer:
    company = "Google"

    def employee(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language

    def getDetails(self):
        print(f"Company : {self.company}")
        print(f"Name of Employee is {self.name}")
        print(f"Salary of Employee is {self.salary}")
        print(f"Language the Employee work with {self.language}")


sreekar = Programmer()

sreekar.employee("Sreekar", 1000000, "Python")
sreekar.getDetails()


# Creating same program using __init__ function , By this we can initialize
# directly using the class

class AnotherProgrammer:
    company = "Google"

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language

    def getDetails(self):
        print(f"Company : {self.company}")
        print(f"Name of Employee is {self.name}")
        print(f"Salary of Employee is {self.salary}")
        print(f"Language the Employee work with {self.language}")


sreekar = AnotherProgrammer("Sreekar", 10000000, "Python")

sreekar.getDetails()
