# Given a student score, determine the of a student
# A | score >= 90
# B | score >= 80
# C | score >= 70
# D | score >= 60
# F | score < 60

score = float(input("Please enter yout score for the test:"))

if score >= 90:
    print("Your grade is A")
elif score >= 80:
    print("Your grade is B")
elif score >= 70:
    print("Your grade is C")
elif score >= 60:
    print("Your grade is D")
else:
    print("Your grade is F")
