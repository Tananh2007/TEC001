def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
my_list = [5, 3, 4, 2, 1]
result = calculate_sum(my_list)

print("The list is:", my_list)
print("The sum of the numbers in the list is:", result)