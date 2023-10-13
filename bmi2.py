print("BMI Calculator")
weight = int(input("Enter your weight in kg"))
height = int(input("Enter your weight in cm"))
height2 = height/100
print("Your height in meters", height2)
height3 = height2*height2
bmi = weight/height3
print("Your BMI is: ", bmi) 
if bmi<18.5:
    print("Underweight")
elif bmi >=18.5 and bmi <=24.9:
    print("Normalweight")
elif bmi >=24.9 and bmi <=29.9:
    print("overweight")
else:
    print("obese")

