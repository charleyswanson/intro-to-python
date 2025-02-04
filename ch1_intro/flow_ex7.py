# Write a function that takes a single integer argument and prints a 
# message that describes whether:

# the value is between 0 and 50 (inclusive)
# the value is between 51 and 100 (inclusive)
# the value is greater than 100
# the value is less than 0

new_number = input('how about a number? ')

def evaluator(digits):
    if int(digits) >= 0 and int(digits) <= 50:
        print('the value is between 0 and 50 (inclusive)')
    elif int(digits) >= 51 and int(digits) <= 100:
        print('the value is between 51 and 100 (inclusive)')
    elif int(digits) > 100:
        print('the value is greater than 100')
    else:
        print('the value is less than 0')

evaluator(new_number)