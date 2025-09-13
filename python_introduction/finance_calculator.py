monthly_income = int(input("Enter your monthly income:"))
total_monthly = int(input("Enter your total monthly expenses:"))

monthly_savings = monthly_income - total_monthly 

projected_savings = (monthly_savings * 12) + (monthly_savings *12 * 0.05)


print(f"your monthly savings is {monthly_savings}")

print(f"your projected savings is { projected_savings}")
