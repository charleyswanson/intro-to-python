# Write Python code to create a new tuple from (1, 2, 3, 4, 5). 
# The new tuple should be in reverse order from the original. 
# It should also exclude the first and last members of the original. 
# The result should be the tuple (4, 3, 2).

my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
my_list.reverse()
short_list = my_list[1:4]
final = tuple(short_list)
print(final)

# rev_list = list(reversed(my_list[1:4]))
# rev_tuple = tuple(rev_list)
