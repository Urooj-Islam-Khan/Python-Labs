# write a program which prompts a user for a Celsius tempreture, convert the tempreture to Fahrenheit and print out the converted tempreture.

temp_C = float(input("Enter tempreture in Celsius: "))

temp_F = (temp_C * 9) / 5 + 32

print("Tempreture in Fahrenheit: " + str(temp_F))
