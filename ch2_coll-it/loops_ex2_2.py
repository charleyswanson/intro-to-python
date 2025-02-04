# Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter. The updated code should use a for loop to display the future ages.

# take an input that asks how old someone is
# print "you're X years old"
# print "in 10, 20, etc years, you'll be X years old"

current_age = int(input('How old are ya? '))
print()
print(f'Right now you\'re {current_age} years old.')
print()
for more_years in range(10, 60, 10):
    print(f'In {more_years} years, you\'ll be {current_age + more_years} old!')
