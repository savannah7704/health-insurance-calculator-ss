print("")
print("Health Insurance Risk Calculator")
print("")
print("This test will determine the risk of insuring a new customer. The higher the number of points, the higher the risk.")
print("")
print("")

points = 0

question1 = str(input("What is the customer's age?"))
answer1 = int(question1)

print (question1)
if answer1 < 30:
    points = points
    print("Points: ", points)
elif answer1 < 45:
    points = points + 10
    print("Points: ", points)
elif answer1 <= 60:
    points = points + 20
    print("Points: ", points)
elif answer1 > 60:
    points = points + 75
    print("Points: ", points)

pounds = float(input("What is the customer's weight in pounds?"))
question2 = pounds
print (question2)
kilograms = pounds * 0.453592
print(pounds, "lbs are equivalent to ", kilograms, "kg")
feet = float (input("What is the customer's height in feet?"))
question3 = feet
print(question3)
meters = feet * 0.3048
print (feet, "ft are equivalent to ", meters, "m")
metersSquared = meters * meters
bmi = kilograms / metersSquared
roundedBmi = round(bmi, 2)
print("The customer's BMI is ", roundedBmi)

if roundedBmi >= 18.5 and roundedBmi <= 24.9:
    print("The customer's BMI falls into the normal category.")
    points = points + 0
    print("Points: ", points)
elif roundedBmi > 24.9 and roundedBmi <= 29.9:
    print("The customer's BMI falls into the overweight category.")
    points = points + 30
    print("Points: ", points)
elif roundedBmi > 29.9:
    print("The customer's BMI falls into the obese category.")
    points = points + 75
    print("Points: ", points)
    


