# ============================================================
# Project Title : Daily Calorie Tracker CLI
# Author        : Arbaaz Ali
# Date          : 05 October 2025
# Course        : Programming for Problem Solving using Python
# ============================================================

import datetime

print("\n===========================================")
print("   Welcome to the Daily Calorie Tracker!   ")
print("===========================================\n")
print("This tool helps you record your daily meals,")
print("track your total calorie intake, and compare")
print("it against your personal daily calorie limit.\n")

# ---------------------------
# Task 2: Input & Data Collection
# ---------------------------

meal_names = []
meal_calories = []

try:
    num_meals = int(input("Enter how many meals you want to log today: "))
except ValueError:
    print("Invalid input! Please enter a number.")
    exit()

for i in range(num_meals):
    print(f"\nMeal {i+1}:")
    meal = input("Enter meal name: ").strip().capitalize()
    try:
        cal = float(input("Enter calories for this meal: "))
    except ValueError:
        print("Invalid calorie input! Please enter a number.")
        exit()
    meal_names.append(meal)
    meal_calories.append(cal)

# ---------------------------
# Task 3: Calorie Calculations
# ---------------------------

total_calories = sum(meal_calories)
average_calories = total_calories / len(meal_calories)

try:
    daily_limit = float(input("\nEnter your daily calorie limit: "))
except ValueError:
    print("Invalid input! Please enter a number.")
    exit()

# ---------------------------
# Task 4: Exceed Limit Warning System
# ---------------------------

if total_calories > daily_limit:
    status_message = "⚠️ You have exceeded your daily calorie limit!"
else:
    status_message = "✅ You are within your daily calorie limit. Keep it up!"

# ---------------------------
# Task 5: Neatly Formatted Output
# ---------------------------

print("\n===========================================")
print("            DAILY CALORIE SUMMARY           ")
print("===========================================\n")
print("Meal Name\t\tCalories")
print("-------------------------------------------")

for i in range(len(meal_names)):
    print(f"{meal_names[i]:<15}\t{meal_calories[i]:>6.2f}")

print("-------------------------------------------")
print(f"Total:\t\t\t{total_calories:.2f}")
print(f"Average per meal:\t{average_calories:.2f}\n")
print(status_message)
print("\n===========================================\n")

# ---------------------------
# Task 6 (Bonus): Save Session Log to File
# ---------------------------

save = input("Do you want to save this session? (yes/no): ").lower().strip()

if save == "yes":
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"calorie_log_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("===========================================\n")
        file.write("           DAILY CALORIE TRACKER LOG        \n")
        file.write("===========================================\n\n")
        file.write(f"Date & Time: {datetime.datetime.now()}\n\n")
        file.write("Meal Name\tCalories\n")
        file.write("-------------------------------------------\n")
        for i in range(len(meal_names)):
            file.write(f"{meal_names[i]:<15}\t{meal_calories[i]:>6.2f}\n")
        file.write("-------------------------------------------\n")
        file.write(f"Total:\t\t{total_calories:.2f}\n")
        file.write(f"Average:\t{average_calories:.2f}\n\n")
        file.write(f"Status: {status_message}\n")
        file.write("===========================================\n")

    print(f"\n✅ Session saved successfully as {filename}\n")
else:
    print("\nSession not saved. Thank you for using the tracker!\n")


#  Sample Run 1

# ===========================================
#    Welcome to the Daily Calorie Tracker!
# ===========================================

# This tool helps you record your daily meals,
# track your total calorie intake, and compare
# it against your personal daily calorie limit.

# Enter how many meals you want to log today: 3

# Meal 1:
# Enter meal name: Breakfast
# Enter calories for this meal: 350

# Meal 2:
# Enter meal name: Lunch
# Enter calories for this meal: 600

# Meal 3:
# Enter meal name: Dinner
# Enter calories for this meal: 500

# Enter your daily calorie limit: 1600

# ===========================================
#             DAILY CALORIE SUMMARY
# ===========================================

# Meal Name        Calories
# -------------------------------------------
# Breakfast          350.00
# Lunch              600.00
# Dinner             500.00
# -------------------------------------------
# Total:            1450.00
# Average per meal: 483.33

# ✅ You are within your daily calorie limit. Keep it up!
# ===========================================

# Do you want to save this session? (yes/no): no

# Session not saved. Thank you for using the tracker!

# ----------------------------------------------------------------------------------------------------------------------

# Sample run 2

# ===========================================
#    Welcome to the Daily Calorie Tracker!
# ===========================================

# Enter how many meals you want to log today: 4

# Meal 1:
# Enter meal name: Coffee
# Enter calories for this meal: 120

# Meal 2:
# Enter meal name: Sandwich
# Enter calories for this meal: 400

# Meal 3:
# Enter meal name: Pizza
# Enter calories for this meal: 850

# Meal 4:
# Enter meal name: Juice
# Enter calories for this meal: 180

# Enter your daily calorie limit: 1300

# ===========================================
#             DAILY CALORIE SUMMARY
# ===========================================

# Meal Name        Calories
# -------------------------------------------
# Coffee             120.00
# Sandwich           400.00
# Pizza              850.00
# Juice              180.00
# -------------------------------------------
# Total:            1550.00
# Average per meal: 387.50

# ⚠️ You have exceeded your daily calorie limit!
# ===========================================

# Do you want to save this session? (yes/no): yes
# ✅ Session saved successfully as calorie_log_2025-10-05_14-50-10.txt

# ------------------------------------------------------------------------------------------------------------------------

# Sample Run 3

# ===========================================
#    Welcome to the Daily Calorie Tracker!
# ===========================================

# Enter how many meals you want to log today: 2

# Meal 1:
# Enter meal name: Breakfast
# Enter calories for this meal: 420

# Meal 2:
# Enter meal name: Dinner
# Enter calories for this meal: 380

# Enter your daily calorie limit: 800

# ===========================================
#             DAILY CALORIE SUMMARY
# ===========================================

# Meal Name        Calories
# -------------------------------------------
# Breakfast          420.00
# Dinner             380.00
# -------------------------------------------
# Total:             800.00
# Average per meal: 400.00

# ✅ You are within your daily calorie limit. Keep it up!
# ===========================================

# Do you want to save this session? (yes/no): no

# Session not saved. Thank you for using the tracker!


