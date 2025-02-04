# Rewrite your code from the previous exercise to use a ternary expression.

import random
random_number = random.randint(0, 4)

# if random_number:
#     print(f'random_number is {random_number} - Yes!')
# else:
#     print(f'random_number is {random_number} - No.')

print('Yes!' if random_number else 'No.')