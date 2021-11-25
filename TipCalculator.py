#define and set variables from user input (casted to a float)
bill = float(input("How mich is the meal?"))
tax = float(input("What is the sales tax (percentage)?"))
tip = float(input("How much of a tip (percentage)?"))

#calculate and add tax
tax_amount = (bill * tax) / 100
total = bill + tax_amount

#calculate and add tip
tip_amount = (total * tip) / 100
total = total + tip_amount

#round thee total to 2 decimal places
total = round(total, 2)

#print the final amount
print("The total bill in $", total, sep = '')
