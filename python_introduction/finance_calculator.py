income = input("Enter your monthly income:")
expenses = input("Enter your total monthly expenses:")
Monthly_Savings = int(income) - int(expenses) 
rate = 0.05
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)
print("Your monthly savings are $", Monthly_Savings) 
print("Projected savings after one year, with interest, is: $",Projected_Savings )