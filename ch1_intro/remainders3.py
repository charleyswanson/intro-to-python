#   Use this function to determine which of the following lists contains at least 
#   one number that is not evenly divisible by 3 (that is, the remainder is not 0):

def remainders_3(numbers):
    return [number % 3 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6]  # True
numbers_2 = [1, 2, 4, 5]           # True
numbers_3 = [0, 3, 6]              # False
numbers_4 = []                     # False

print(any(remainders_3(numbers_1)))
print(any(remainders_3(numbers_2)))
print(any(remainders_3(numbers_3)))
print(any(remainders_3(numbers_4)))