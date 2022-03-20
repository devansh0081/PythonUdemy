print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height>=120 :
  print("You can ride")
  age=int(input("What is your age ? "))
  if age<12:
    print("Child ticket will cost $5")
  elif age<=18:
    print("Youth ticket will cost $10")
  else:
    print("Adult ticket will cost $15")
else:
  print("You cannot ride")