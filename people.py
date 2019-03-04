class Person:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return (f"Hello my name is {self.name}.")

class Student(Person):

    def learn(self):
        return "I get it!"

class Instructor:

    def teach(self):
        return "An object is an instance of a class."


chris = Student('Chris')
nadia = Instructor('Nadia')

print(chris.__str__())
print(nadia.__str__())

print(chris.learn())
print(nadia.teach())

print(chris.teach())  # no teach method on Chris
