# Count the number of elements in scores that are 100 or above.

scores = [96, 47, 113, 89, 100, 102]

# count = sum(1 for num in scores if num >= 100)
# print(count)

total = 0
for score in scores:
    if score >= 100:
        total += 1

print(total)
