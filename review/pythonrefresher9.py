import datetime

class Car:
    def __init__(self, year, maker, model):
        self.year = year
        self.maker = maker
        self.model = model

    def get_age(self):
        now = datetime.datetime.now()
        return int(now.year) - self.year


mycar = Car(1989, "VW", "Beetle")
print(mycar.get_age())
