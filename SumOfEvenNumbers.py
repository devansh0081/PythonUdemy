#Write your code below this row 👇
sum_of_even_numbers=0
for number in range(2,101,2):
  print(number)
  sum_of_even_numbers+=number
print(f"The sum of even numbers in the range 1 to 100 is : {sum_of_even_numbers}")