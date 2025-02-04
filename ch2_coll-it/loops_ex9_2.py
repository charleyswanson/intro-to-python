# Write a function that computes and returns the factorial of a number by using a for or while loop. The factorial of a positive integer n, signified by n!, is defined as the product of all integers between 1 and n, inclusive:

# n!	Expansion	        Result
# 1!	1	                1
# 2!	1 * 2	            2
# 3!	1 * 2 * 3	        6
# 4!	1 * 2 * 3 * 4	    24
# 5!	1 * 2 * 3 * 4 * 5	120


def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

print(factorial(1))   # 1
print(factorial(2))   # 2
print(factorial(3))   # 6
print(factorial(4))   # 24
print(factorial(5))   # 120
print(factorial(6))   # 720
print(factorial(7))   # 5040
print(factorial(8))   # 40320
print(factorial(25))  # 15511210043330985984000000