p = input("Enter the loan amount ")
n = input("Enter the mortgage duration(in months) ")
r = input("Enter the rate of interest ")

r = r/1200

m = (r * p * ((1+r)**n)) / (((1+r)**n) - 1)

print("The monthly payment for a loan of amount of {} over a period of {} at {} is {}.".format(p, n, r, m))