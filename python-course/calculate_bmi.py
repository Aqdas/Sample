print("This program calculates your body mass index.")
height = float (input("Please enter your height in meters: "))
weight = float (input("Please enter your weight in kilo's: "))
BMI = weight/(height**2)
print("Your BMI is: ", round(BMI, 2))

if (BMI <= 18.5):
  classification = "Underweight"
elif (BMI > 18.5 and BMI <= 24.9):
  classification = "Normal weight"
elif (BMI > 24.9 and BMI <= 29.9):
  classification = "Overweight"
else:
  classification = "Obesity"
print ("The classification of your BMI is: ", classification)