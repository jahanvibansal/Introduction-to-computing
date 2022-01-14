a=float(input("Gross income is "))
b=int(input("Number of dependents is "))
taxable_income=a-10000-(3000*b)
tax=taxable_income*0.2
print("income tax= ", tax)