print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
pay = round((bill + bill*(tip/100))/split, 2)
final = "{:.2f}".format(pay)  # Formatting adds zero in decimal place
print(f"Each person should pay: ${final}")
