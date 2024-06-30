import tkinter as tk
import random

fruits = ["Apple", "Banana", "Cherry", "Date", "Fig", "Grape", "Kiwi","strawberry"]
proteins = ["Chicken", "Beef", "Tofu", "Salmon", "Eggs", "Beans", "Tempeh","soya chunks"]
vegetables = ["Carrot", "Broccoli", "Spinach", "Pepper", "Cucumber", "Zucchini", "Tomato","bit"]
grains = ["Rice", "Quinoa", "Pasta", "Bread", "Couscous", "Barley", "Oats",]

def generate_combination():
    fruit = random.choice(fruits)
    protein = random.choice(proteins)
    vegetable = random.choice(vegetables)
    grain = random.choice(grains)
    combination = f"{fruit}, {protein}, {vegetable}, and {grain}"
    combination_label.config(text=combination)

root = tk.Tk()
root.title("Random Food Combination Generator")
root.geometry("400x300")

combination_label = tk.Label(root, text="", font=("Helvetica", 16), wraplength=350)
combination_label.pack(pady=20)

generate_button = tk.Button(root, text="Generate Combination", command=generate_combination)
generate_button.pack(pady=20)

root.mainloop()

