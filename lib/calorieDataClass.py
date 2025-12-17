import date

class calorieData:
    def __init__(self):
        self.foodDict = {} # will map dates to foods eaten 
        self.calorieDict = {}
    def add_meal(self, food_name, calories):
        if self.calorieDict.get(date.today()) is None:
            self.calorieDict[date.today()] = 0
        self.calorieDict[date.today()] += calories

        if self.foodDict.get(date.today()) is None:
            self.foodDict[date.today()] = []    
        if food_name not in self.foodDict[date.today()]:
            self.foodDict[date.today()].append(food_name)