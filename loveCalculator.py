# Method 1

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
new_name1=name1.lower()
new_name2=name2.lower()
T_count=new_name1.count("t")+new_name2.count("t")
R_count=new_name1.count("r")+new_name2.count("r")
U_count=new_name1.count("u")+new_name2.count("u")
E_count=new_name1.count("e")+new_name2.count("e")
TRUE_count=T_count+R_count+U_count+E_count
L_count=new_name1.count("l")+new_name2.count("l")
O_count=new_name1.count("o")+new_name2.count("o")
V_count=new_name1.count("v")+new_name2.count("v")
E_count=new_name1.count("e")+new_name2.count("e")
LOVE_count=L_count+O_count+V_count+E_count
print("Your love percentage is "+str(TRUE_count)+str(LOVE_count))

# Method 2

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
