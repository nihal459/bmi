def calcu(w,h):
    heightinmeters = h/100
    print("Your height in meters", heightinmeters)
    newheight = heightinmeters*heightinmeters
    bmi = w/newheight
    return bmi

def bmi_value(bmi):
    if bmi<18.5:
        print("Underweight")
    elif bmi >=18.5 and bmi <=24.9:
        print("Normalweight")
    elif bmi >=24.9 and bmi <=29.9:
        print("overweight")
    else:
        print("obese")

print("BMI Calculator")
weight = int(input("Enter your weight in kg"))
height = int(input("Enter your weight in cm"))
bmi = calcu(weight,height)
print(bmi)
bmi_value(bmi)



