height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi=round(weight/(height*height))
if bmi<18.5:
  print("You are underweight")
elif bmi<25:
  print("You have normal weight")
elif bmi<30:
  print("You are overweight")
elif bmi<35:
  print("You are obese")
else:
  print("You are clinically obese")