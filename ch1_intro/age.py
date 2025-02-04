age = input('How old are you? ')
print(f'You are {age} years old.')
for i in range(1,5):
    years = i*10
    print(f'In {years} years, you will be {int(age) + years} years old.')