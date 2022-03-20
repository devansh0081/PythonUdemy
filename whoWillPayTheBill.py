import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")

list_length=len(names)-1
random_number=random.randint(0,list_length)

person_who_will_pay = names[random_number]
print(person_who_will_pay + " is going to buy the meal today!")

#choice fnc will do the same easliy but here we wanted to learn about indices