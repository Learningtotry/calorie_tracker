

# will use tkinter to build a simple Calorie tracker
# will store data using pickle in a file
# use matplotlib to plot calorie intake over time

# right now in conda environment calorie_tracker

import os
import matplotlib.pyplot as plt
import tkinter as tk
import pickle

from lib import *

tempFood = {"apple": 95, "banana": 105, "sandwich": 250}


pickle.dump(1, open("assets/data_file.pkl", "wb"))
pickle.dump(tempFood, open("assets/calorie_data.pkl", "wb"))
# the data_file will have a list of days with calorie intakes listed next to them
class food:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories



class CalorieTracker:
    def __init__(self, root, foodList, calorieList):
        self.root = root
        self.root.title("Calorie Tracking app")
        self.data_file = os.path.join("assets", "data_file.pkl")
        self.calorie_file = os.path.join("assets", "calorie_data.pkl")
        self.foods = pickle.load(open(self.calorie_file, "rb"))
        self.calories = pickle.load(open(self.data_file, "rb"))
    def save_data(self):
        with open(self.calorie_file, "wb") as f:
            pickle.dump(self.calories, f)
        with open(self.data_file, "wb") as f:
            pickle.dump(self.foods, f)

myTracker = CalorieTracker(tk.Tk())
myTracker.save_data()
myTracker.root.mainloop()
