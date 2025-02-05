# Write a function that returns the last element of a list provided as an argument. For example:

def last(new_list):
    if new_list:
        return new_list[-1]
    else:
        return None

print(last(['Earth', 'Moon', 'Mars']))  # Mars
print(last([]))  # 