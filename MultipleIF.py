print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0
if height>=120 :
  print("You can ride")
  age=int(input("What is your age ? "))
  if age<12:
    bill=5
    print("Child ticket will cost $5")
  elif age<=18:
    bill=10
    print("Youth ticket will cost $10")
  else:
    bill=15
    print("Adult ticket will cost $15")
  wants_photo=input("Do you want a photo taken ? Y or N ")  
  if wants_photo=="Y":
    bill +=3
    print(f"Your total bill is ${bill}")
else:
  print("You cannot ride")