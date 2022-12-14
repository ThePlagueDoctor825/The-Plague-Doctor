import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 10
        self.alive = True


    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out")
            self.alive = False

        elif self.gladness <= 0:
            print("Depression")
            self.alive = False
        elif self.progress > 5:
            print("Done!")
            self.alive = False
    def work(self):
        if self.gladness >= 110:
            self.money += 30
            print("Student get money")
    def student_money(self):
        if self.money <= 0:
            print("you got into debt")
            self.alive = False
        elif self.money >= 0:
            print("Nice")
    def spend_money(self):
        if self.money >= 200:
          self.money -= random.randint(20,200)

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money}")

    def life(self, day):
        day = "Day" +str(day)+"of"+self.name+"life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.work()
        self.end_of_day()
        self.is_alive()


JoeBiden = Student(name="Joe Biden")
for day in range(365):
    if JoeBiden.alive == False:
        break
    JoeBiden.life(day)