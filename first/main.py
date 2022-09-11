import random

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.dladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        pass

    def get_job(self):
        pass

    def get_car(self):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def shopping(self, manage):
        pass

    def chill(self):
        pass

    def clean_home(self):
        pass

    def to_repair(self):
        pass

    def days_indexes(self,day):
        pass

    def is_alive(self):
        pass

    def live(self, day):
        pass

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strenght = brand_list[self.brand]["strenght"]
        self.consumtion = brand_list[self.brand]["consumtion"]

a=[1,2,]
b=a[5]

Brands_of_car = {'BMW': {'fuel': 100, 'strength': 100, 'consumption': 6},'Audio': {'fuel': 50, 'strength': 40, 'consumption': 6}

}



