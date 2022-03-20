# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
#Write your code below this row 👇
total_height=0
for height in student_heights:
  total_height=total_height+height
  
total_length=0
for length in student_heights:
  total_length=total_length+1 

avg_height=round(total_height/total_length)
print(avg_height)

# here we can use len and sum function but currently we are learning the use of loops