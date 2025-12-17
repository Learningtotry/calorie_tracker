
# will use tkinter to build a simple Calorie tracker
# will store data using pickle in a file
# use matplotlib to plot calorie intake over time

import os
import matplotlib.pyplot as plt
import tkinter as tk
import pickle

from lib import *


class CalorieTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Calorie Tracking app")
        self.data_file = os.path.join("assets", "data_file.pkl")
        if (os.path.getsize(self.data_file)) == 0:
            self.calorieData = calorieDataClass()
        else:
            self.calorieData = pickle.load(open(self.data_file, "rb"))
        self.foods = self.calorieData.foodDict
        self.calories = self.calorieData.calorieDict

        self.window = window("Calorie Tracker", 400, 600, self.calorieData, self.root)


    def save_data(self):
        with open(self.data_file, "wb") as f:
            pickle.dump(self.calorieData, f)

myTracker = CalorieTracker(tk.Tk())

while True:
    myTracker.window.run()
    myTracker.root.mainloop()
    myTracker.save_data()
    break

