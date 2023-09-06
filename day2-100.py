#second day project

#Tip calculator

#Welcome to the tip calculator
print("Welcome to the tip calculator!")

#collecting data from input
#What was the total bill? $124.56
bill=float(input("What was the total bill?"))

#How many people to split the bill? 5
people=int(input("How many people to split the bill?"))

#What percentage tip would you like to give? 10, 12, or 15? 12
tip=int(input("What percentage tip would you like to give? 10, 12  or 15"))
tip_perc=tip/100*bill+bill
print(tip_perc)
print(f"Each person should pay: $ ", tip_perc/people)
#Each person should pay: $27.9

