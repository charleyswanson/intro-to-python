# Write a function, even_or_odd, that determines whether its argument is an even or odd number. If it's even, the function should print 'even'; otherwise, it should print 'odd'. Assume the argument is always an integer.

# def even_or_odd(number):
#     if number % 2 == 0:
#         return(f'{number} is even')
#     else:
#         return(f'{number} is odd')
    
def even_or_odd(number):
    return (f'{number} is even') if number % 2 == 0 else (f'{number} is odd')

test = int(input('how about a number? '))
print(even_or_odd(test))