# Determining is someone qualifies for a loan
salary_per_annum = float(input("Enter your salary per annum:"))
employment_period = int(input("Enter employment period in years:"))

if salary_per_annum >= 30000:
    if employment_period >= 2:
        print("You qualify for a loan")
    else:
        print("You do not qualify")
else:
    print("You do not qualify for a loan")