#  Write a Python function to sum all the numbers in a list.

total = 0
ele = 0

list1 = [8, 2, 3, 0, 7]

while ele < len(list1):
    total = total + list1[ele]
    ele += 1

print(total)
