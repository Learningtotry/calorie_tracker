# the purpose of this file will be to render the GUI for the calorie tracker

from tkinter import *
from tkinter import ttk
from datetime import date


class _FoodWindow():
        def __init__(self, root, foodDict):
            self.root = root

            self.foodDict = foodDict

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

                foodDict[food_name_entry.get()] = int(food_calorie_entry.get())
                input_win.destroy()
                return
            submit_button = Button(input_win, text="Enter", command=submit)
            submit_button.grid(row=2, column=0, columnspan=2, pady=10)



class _CalorieWindow():
    def __init__(self, root, calorieDict, foodDict):
        self.root = root
        self.calorieDict = calorieDict
        self.foodDict = foodDict
        input_win = Toplevel(self.root)
        input_win.title("Add food for the day")
        input_win.geometry("300x400")

        ttk.Label(input_win, text="Food item:").grid(row=0, column=0, padx=10, pady=10)
        food_entry = Spinbox(input_win, values=list(self.foodDict.keys()))
        food_entry.grid(row=0, column=1, padx=10)

        def add_calorie():
            self.calorieDict[date.today()] += self.foodDict[food_entry.get()] # add the calories for this food
            input_win.destroy()
            print("Calorie amount was: ", self.calorieDict[date.today()])
            return
        ttk.Button(input_win, text="Add calories", command=add_calorie).grid(row=2, column=0, columnspan=2, pady=10)

        submit_button = Button(input_win, text="Enter", command=add_calorie)
        submit_button.grid(row=1, column=0, columnspan=2, pady=10)


class window():
    def __init__(self, title, width, height, calorieData, root):
        self.foodDict = calorieData.foodDict
        self.calorieDict = calorieData.calorieDict
        self.foodsTodayDict = calorieData.foodsTodayDict

        self.root = root
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")

        self.mainFrame = ttk.Frame(self.root, padding="10")
        self.mainFrame.grid(row=0, column=0, sticky=(N, S, E, W))
        self.mainFrame.columnconfigure(0, weight=1)
        self.mainFrame.columnconfigure(1, weight=1)

        self.leftFrame = ttk.Frame(self.mainFrame, borderwidth=2, relief="sunken")
        self.leftFrame.grid(row=0, column=0, rowspan=4, sticky=(N, S, E, W), padx=10, pady=10)
        self.plotFrame = ttk.Frame(self.leftFrame, padding=(3, 3, 12, 12))
        self.plotFrame.grid(row=0, column=0, sticky=(N, E, S, W))

        ttk.Label(self.plotFrame, text="Calorie Tracker", font=("Helvetica", 16)).grid(row=0, column=0, pady=10)
        #message = ttk.Label(self.root, text="Calorie tracker")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.mainFrame.columnconfigure(0, weight=1)
        #self.mainFrame.rowconfigure(0, weight=1) won't use roots rows
        
        ttk.Button(self.leftFrame, text="Add Food", command = self.add_food).grid(row=2, column=0, pady=10)
        ttk.Button(self.leftFrame, text="Add calories", command = self.add_calories).grid(row=3, column=0, pady=10)

        self.rightFrame = ttk.Frame(self.mainFrame, borderwidth=2, relief="sunken")
        self.rightFrame.grid(row=0, column=1, rowspan=4, sticky=(N, S, E, W), padx=10, pady=10)
        self.caloriesTodayVar = StringVar()
        self.caloriesTodayVar.set(self.calorieDict[date.today()] if date.today() in self.calorieDict.keys() else "")
        self.upRightFrame = ttk.Frame(self.rightFrame)
        self.upRightFrame.grid(row=0, column=0, padx=10, pady=10)
        Label(self.upRightFrame, text="Calories today:").grid(row=0, column=0, padx=10, pady=10)
        Label(self.upRightFrame, textvariable=self.caloriesTodayVar).grid(row=1, column=0, padx=10, pady=10)
        self.lowerRightFrame = ttk.Frame(self.rightFrame)
        self.lowerRightFrame.grid(row=1, column=0, padx=10, pady=10)
        Label(self.lowerRightFrame, text="Foods eaten today:").grid(row=0, column=0, padx=10, pady=10)
        foodsEatenToday = self.foodDict.get(date.today(), [])
        self.foodsEatenTodayVar = StringVar()
        self.foodsEatenTodayVar.set(", ".join(foodsEatenToday))

        Label(self.lowerRightFrame, textvariable=self.foodsEatenTodayVar, wraplength=200).grid(row=1, column=0, padx=10, pady=10)
        #foodsEatenTodayVar.set("asdf")



    def add_food(self):
        window = _FoodWindow(self.root, self.foodDict)

    def run(self):
        self.root.mainloop()

    def add_calories(self):
        if self.calorieDict.get(date.today()) is None:
            self.calorieDict[date.today()] = 0
        if self.foodsTodayDict.get(date.today()) is None:
            self.foodsTodayDict[date.today()] = []
        window = _CalorieWindow(self.root, self.calorieDict, self.foodsTodayDict)

        foodsEatenToday = self.foodsTodayDict.get(date.today())
        print("Foods eaten today are: ", foodsEatenToday)
        self.foodsEatenTodayVar.set(", ".join(foodsEatenToday))
        #self.foodsEatenTodayVar.set("asdf")
        #self.foodsEatenTodayVar.set("asdf")
        #print("reached here at least")
