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

if answer1.isdigit():
    print("")

    answer1 = int(question1)
else:
    print("Please enter the customer's age with a number.")

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

question4 = str(input("What is the customer's systolic blood pressure?"))
answer4 = int(question4)
print(question4)
question5 = str(input("What is the customer's diastolic blood pressure?"))
answer5 = int(question5)
print(question5)

if answer4 < 120 and answer5 < 80:
    print("The customer's blood pressure is in the normal category.")
    points = points
    print("Points: ", points)
elif answer4 >= 120 and answer4 <= 129 and answer5 < 80:
    print("The customer's blood pressure is in the elevated category.")
    points = points + 15
    print("Points: ", points)
elif answer4 >= 130 and answer4 <= 139 or answer5 >= 80 and answer5 <= 89:
    print("The customer's blood pressure is in the stage 1 category.")
    points = points + 30
    print("Points: ", points)
elif answer4 >= 140 and answer4 < 180 or answer5 >= 90 and answer5 < 120:
    print("The customer's blood pressure is in the stage 2 category.")
    points = points + 75
    print("Points: ", points)
elif answer4 >= 180 or answer5 >= 120:
    print("The customer's blood pressure is in the crisis range.")
    points = points + 100
    print("Points: ", points)
    
#To do: ask about history of family diseases and calculate total score

question6 = str(input("Does the customer have a family history of diabetes?"))
answer6 = str(question6)
print(question6)

if answer6 == "yes" or answer6 == "Yes" or answer6 == "YES" or answer6 == "y" or answer6 == "Y":
    points = points + 10
    print("Points: ", points)
elif answer6 == "no" or answer6 == "No" or answer6 == "NO" or answer6 == "n" or answer6 == "N":
    points = points
    print("Points: ", points)

question7 = str(input("Does the customer have a family history of cancer?"))
answer7 = str(question7)
print(question7)

if answer7 == "yes" or answer7 == "Yes" or answer7 == "YES" or answer7 == "y" or answer7 == "Y":
    points = points + 10
    print("Points: ", points)
elif answer7 == "no" or answer7 == "No" or answer7 == "NO" or answer7 == "n" or answer7 == "N":
    points = points
    print("Points: ", points)

question8 = str(input("Does the customer have a family history of Alzheimer’s?"))
answer8 = str(question8)
print(question8)

if answer8 == "yes" or answer8 == "Yes" or answer8 == "YES" or answer8 == "y" or answer8 == "Y":
    points = points + 10
    print("Points: ", points)
elif answer8 == "no" or answer8 == "No" or answer8 == "NO" or answer8 == "n" or answer8 == "N":
    points = points
    print("Points: ", points)
    
print("Total points: ", points)
if points <= 20:
    print("Based on the responses, the customer is low risk.")
elif points <= 50:
    print("Based on the responses, the customer is moderate risk.")
elif points <= 75:
    print("Based on the responses, the customer is high risk.")
elif points > 75:
    print("Based on the responses, the customer is uninsurable.")