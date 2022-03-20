
two_digit_number = input("Type a two digit number: ")
#first we will subscript the digits so that we can add them seperately
first_digit=two_digit_number[0]
second_digit=two_digit_number[1]
# now we cant add them directly because they are strings so there will be no use so first we will convert them into integer
new_first_digit=int(first_digit)
new_second_digit=int(second_digit)
#now concatenate and print the result
print(new_first_digit+new_second_digit)






