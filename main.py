

# will use tkinter to build a simple Calorie tracker
# will store data using pickle in a file
# use matplotlib to plot calorie intake over time

# right now in conda environment calorie_tracker


import matplotlib.pyplot as plt
import tkinter as tk
import pickle


# the data_file will have a list of days with calorie intakes listed next to them
class food:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories



class CalorieTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Calorier Tracking app")
        self.data_file = "calorie_data.pkl"
        self.calorie_data = self.load_data()
        self.food_calories = self
        foods = pickle.load(open("food_calories.pkl", "rb"))
    def __del__(self):
        pickle.dump(self.calorie_data, open(self.data_file, "wb"))
        pickle.dump(self.food_calories, open("food_calories.pkl", "wb"))

