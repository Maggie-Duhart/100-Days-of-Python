#Calculate the total amount to split a bill based on tip %
#Format the result to 2 decimal places = 33.60

#My Code 👇
print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
split = int(input("How many people to split the bill? "))

result = (total_bill / split) * (tip_percentage / 100 + 1)
round_result = round(result, 2)
round_result = "{:.2f}".format(round_result)  #precision

print(f"Each person should pay: ${round_result}")
