# Write a program to prompt the user for hours and rate per hour to compute gross pay.

Hours = int(input("Enter Hours: "))

Rate = float(input("Enter Rate: "))

gross_pay = Hours * Rate

print("Gross Pay: " + str(gross_pay))
