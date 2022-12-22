gross = int(input("Enter your gross income in dollars :"))
dep = int(input("enter number of dependent :"))
std_dxn = 3000*dep + 10000
tax_icm = gross- std_dxn
tax = tax_icm * 0.2
print("tax:")
print(tax)