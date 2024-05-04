#Example:
#If the bill was $150, split between 5 people, with 12% tip.
#Each person should pay (150.00/5) * 1.12 = 33.6
#Round the result to 2 decimals places = 33.60

print("Welcome to the tip calculator!")
total_bill = float (input("What was the total bill? $"))
tip = float (input("How much tip would you like to give? 10, 12 or 15? "))
people = int (input("How many people to split the bill? "))
bill_with_tip = total_bill + total_bill*(tip/100)
bill_split = round(bill_with_tip / people, 2)
total_split = "{:.2f}".format(bill_split)

print (f"Each person should pay: ${total_split}")
