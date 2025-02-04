# Write a function that returns the first element of a list provided as an argument. For example:

def first(my_list):
    if my_list != []:
        return my_list[0]
    else:
        return None

print(first(['Earth', 'Moon', 'Mars']))  # Earth
print(first([]))  # 