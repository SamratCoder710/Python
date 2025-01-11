import math

print("Welcome to Bill Calculator!")
total_bill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give ? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill?\n"))
total_bill += (tip * total_bill)/100
per_person_bill = round(total_bill/people,2)
print("Each person should pay : $"+per_person_bill)
