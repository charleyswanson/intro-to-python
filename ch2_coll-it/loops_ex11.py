# Print all of the even numbers in the following list of nested lists. This time, don't use any for loops.

# 6
# 4
# 2
# 4
# 16
# 0

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

index = 0
while index < len(my_list):
    list = my_list[index]
    nested_index = 0
    while nested_index < len(list):
        nested_number = list[nested_index]
        if nested_number % 2 == 0:
            print(nested_number)                
        nested_index += 1
    index += 1
