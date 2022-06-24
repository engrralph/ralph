tax_rate = 0.25
standard_deduc = 12400.0
dependent_deduc = 1100.0
# Request the inputs
grossinc = float(input("Enter the gross income: "))
numdep = int(input("Enter the number of dependents: "))
# Compute the income tax
taxableinc = grossinc - standard_deduc - \
dependent_deduc* numdep
inctax = taxableinc * tax_rate
# Display the income tax
print("The income tax is $" + str(inctax))