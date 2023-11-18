import csv

items = {}

with open("rawfruits.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        fruit = row["Fruits"]
        calories = row["Calories"]
        items[fruit] = calories

item = input("Item: ")
if item in items:
    print(f"Calories: {items[item]}")

# for fruit, calories in fruits.items():
# print(f'Fruit: {fruit}, Calories: {calories}')
