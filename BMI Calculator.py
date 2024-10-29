Weight = int(input("Enter your weight in pounds: "))
Height = int(input("Enter your height in inches: "))
BMI = (Weight * 703) / (Height * Height)
print("Your BMI is: ") 
print(BMI)


if BMI>0:
    if(BMI<18.5):
          print("You are underweight.")
    elif (BMI<=24.9):
          print("You are normal weight.")
    elif (BMI<29.9):
          print("You are overweight.")
    elif (BMI<34.9):
          print("You are obese.")
    elif (BMI<39.9):
          print("You are severely obese.")
    else:
          print("Enter valid points")