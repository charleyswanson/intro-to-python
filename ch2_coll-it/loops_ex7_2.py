# Write a find_integers function that returns a list of all the integers from my_tuple:

# print(type(77) is int)        # True


# def find_integers(input):
#     function_list = []
#     for item in input:
#         if type(item) is int:
#             function_list.append(item)
#     return function_list

def find_integers(input):
    return [ item for item in input if type(item) is int ]

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)

print(integers)                    # [1, 3, -4]
