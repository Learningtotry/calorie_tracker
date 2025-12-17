# the purpose of this file will be to render the GUI for the calorie tracker

from tkinter import *
from tkinter import ttk
from datetime import date


class _FoodWindow():
        def __init__(self, root, foodList):
            self.root = root

            self.foodList = foodList

            input_win = Toplevel(self.root)
            input_win.title("Add a food item")
            input_win.geometry("300x200")

            ttk.Label(input_win, text="Food name:").grid(row=0, column=0, padx=10, pady=10)
            ttk.Label(input_win, text="Calories:").grid(row=1, column=0, padx=10, pady=10)
            food_name_entry = Entry(input_win)
            food_calorie_entry = Entry(input_win)
            food_name_entry.grid(row=0, column=1, padx=10)
            food_calorie_entry.grid(row=1, column=1, padx=10)

            def submit():
                food_name = food_name_entry.get()
                print("Food name was: ", food_name, " and calories: ", food_calorie_entry.get())

                foodList[food_name_entry.get()] = food_calorie_entry.get()
                input_win.destroy()
            submit_button = Button(input_win, text="Enter", command=submit)
            submit_button.grid(row=2, column=0, columnspan=2, pady=10)



class _CalorieWindow():
    def __init__(self, root, calorieList, foodList):
        self.root = root
        self.calorieList = calorieList
        self.foodList = foodList
        input_win = Toplevel(self.root)
        input_win.title("Add food for the day")
        input_win.geometry("300x400")

        ttk.Label(input_win, text="Food item:").grid(row=0, column=0, padx=10, pady=10)
        food_entry = Spinbox(input_win, values=self.foodList).grid(row=0, column=1, padx=10)

        def add_calorie():
            self.calorieList[date.today()] += self.foodList[food_entry.get()] # add the calories for this food
            input_win.destroy()
        ttk.Button(input_win, text="Add calories", command=add_calorie).grid(row=2, column=0, columnspan=2, pady=10)


        def submit():
            food = food_entry.get()
            calorie_amount = self.foodList[food]
            print("Calorie amount was: ", calorie_amount)
            input_win.destroy()
        submit_button = Button(input_win, text="Enter", command=submit)
        submit_button.grid(row=1, column=0, columnspan=2, pady=10)


class window():
    def __init__(self, title, width, height, calorieData):
        self.foodList = calorieData.foodDict
        self.calorieList = calorieData.calorieDict

        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")

        self.mainFrame = ttk.Frame(self.root, padding="10")
        self.mainFrame.grid(row=0, column=0, sticky=(N, S, E, W))
        self.plotFrame = ttk.Frame(self.mainFrame, padding=(3, 3, 12, 12))
        self.plotFrame.grid(row=0, column=0, sticky=(N, W))

        ttk.Label(self.plotFrame, text="Calorie Tracker", font=("Helvetica", 16)).grid(row=0, column=0, pady=10)
        message = ttk.Label(self.root, text="Calorie tracker")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.mainFrame.columnconfigure(0, weight=1)
        self.mainFrame.rowconfigure(0, weight=1)
        
        ttk.Button(self.mainFrame, text="Add Food", command = self.add_food).grid(row=2, column=0, pady=10)
        ttk.Button(self.mainFrame, text="Add calories", command = self.add_calories).grid(row=3, column=0, pady=10)
        #self.calculateButton = ttk.Button(self.mainFrame, text="Add food", command = self.add_food)
    def add_food(self):
        window = _FoodWindow(self.root, self.foodList)

    def run(self):
        self.root.mainloop()

    def add_calories(self):
        window = _CalorieWindow(self.root, self.calorieList, self.foodList)
