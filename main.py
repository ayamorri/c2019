class Student:
    group = "C2019"
    gender = "Male"
    education = "MKA STEP"

    def __init__(self, name, age, swim):
        self.name = name
        self.age = age
        self.swim = swim

    def get_swim(self):
        return self.swim


st1 = Student(name="oleg", age=15, swim=True)
st2 = Student(name="anna", age=17, swim=True)
st3 = Student(name="ilya", age=16, swim=False)

print(st1.name)
print(st2.name)
print(st3.name)
print(st1.get_swim())
print(st2.get_swim())
print(st3.get_swim())
