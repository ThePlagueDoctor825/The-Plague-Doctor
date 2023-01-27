class Human:
    health = 100


class Student(Human):
    stronger = 50


class Bum(Human):
    stronger = 25


pers1 = Student()
pers2 = Bum

print(pers1.stronger)
print(pers1.health)


