year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆
if year%4!=0:
  print(f"{year} is not a leap year.")
else:
  if year%100!=0:
    print(f"{year} is a leap year.")
  else:
    if year%400==0:
      print(f"{year} is a leap year.")
    else:
      print(f"{year} is not a leap year.")