from decimal import Decimal

cost = input("Enter the cost of the item ")
tax_rate = input("Enter the tax rate in % ")

tax_rate = (Decimal(tax_rate)/100)

tax = Decimal(cost) * tax_rate

total_cost = tax + Decimal(cost)

print("The total tax is {} and the total cost is {}".format(round(tax, 2), round(Decimal(total_cost), 2)))