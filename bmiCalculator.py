
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi=int(weight)/(float(height)**2)
#height has to be float it is high probability that height has decimal places but weight is generally whole number so we can make it integer instead of float
#now we can convert the bmi into whole number
new_bmi=int(bmi)
print(new_bmi)